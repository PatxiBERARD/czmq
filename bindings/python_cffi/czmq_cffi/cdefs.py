import re
czmq_cdefs = list ()
# Custom setup for czmq
czmq_cdefs.append ('''
typedef int time_t;
typedef int off_t;

typedef unsigned char   byte;           //  Single unsigned byte = 8 bits
typedef unsigned short  dbyte;          //  Double byte = 16 bits
typedef unsigned int    qbyte;          //  Quad byte = 32 bits
typedef int SOCKET;

//  -- destroy an item
typedef void (czmq_destructor) (void **item);
//  -- duplicate an item
typedef void *(czmq_duplicator) (const void *item);
//  - compare two items, for sorting
typedef int (czmq_comparator) (const void *item1, const void *item2);
''')



czmq_cdefs.append ('''
typedef struct _zactor_t zactor_t;
typedef struct _zsock_t zsock_t;
typedef struct _zmsg_t zmsg_t;
typedef struct _zargs_t zargs_t;
typedef struct _zarmour_t zarmour_t;
typedef struct _zchunk_t zchunk_t;
typedef struct _char_t char_t;
typedef struct _zcert_t zcert_t;
typedef struct _zlist_t zlist_t;
typedef struct _zcertstore_t zcertstore_t;
typedef struct _zframe_t zframe_t;
typedef struct _zclock_t zclock_t;
typedef struct _msecs_t msecs_t;
typedef struct _zconfig_t zconfig_t;
typedef struct _zdigest_t zdigest_t;
typedef struct _zdir_t zdir_t;
typedef struct _zhash_t zhash_t;
typedef struct _zdir_patch_t zdir_patch_t;
typedef struct _zfile_t zfile_t;
typedef struct _zhashx_t zhashx_t;
typedef struct _zlistx_t zlistx_t;
typedef struct _ziflist_t ziflist_t;
typedef struct _zloop_t zloop_t;
typedef struct _zmq_pollitem_t zmq_pollitem_t;
typedef struct _zpoller_t zpoller_t;
typedef struct _zproc_t zproc_t;
typedef struct _va_list_t va_list_t;
typedef struct _socket_t socket_t;
typedef struct _zstr_t zstr_t;
typedef struct _ztimerset_t ztimerset_t;
typedef struct _ztrie_t ztrie_t;
typedef struct _zuuid_t zuuid_t;
// Actors get a pipe and arguments from caller
typedef void (zactor_fn) (
    zsock_t *pipe, void *args);

// Loaders retrieve certificates from an arbitrary source.
typedef void (zcertstore_loader) (
    zcertstore_t *self);

// Destructor for loader state.
typedef void (zcertstore_destructor) (
    void **self_p);

// 
typedef int (zconfig_fct) (
    zconfig_t *self, void *arg, int level);

// Callback function for zhash_freefn method
typedef void (zhash_free_fn) (
    void *data);

// Destroy an item
typedef void (zhashx_destructor_fn) (
    void **item);

// Duplicate an item
typedef void * (zhashx_duplicator_fn) (
    const void *item);

// Compare two items, for sorting
typedef int (zhashx_comparator_fn) (
    const void *item1, const void *item2);

// Destroy an item.
typedef void (zhashx_free_fn) (
    void *data);

// Hash function for keys.
typedef size_t (zhashx_hash_fn) (
    const void *key);

// Serializes an item to a longstr.                       
// The caller takes ownership of the newly created object.
typedef char * (zhashx_serializer_fn) (
    const void *item);

// Deserializes a longstr into an item.                   
// The caller takes ownership of the newly created object.
typedef void * (zhashx_deserializer_fn) (
    const char *item_str);

// Comparison function e.g. for sorting and removing.
typedef int (zlist_compare_fn) (
    void *item1, void *item2);

// Callback function for zlist_freefn method
typedef void (zlist_free_fn) (
    void *data);

// Destroy an item
typedef void (zlistx_destructor_fn) (
    void **item);

// Duplicate an item
typedef void * (zlistx_duplicator_fn) (
    const void *item);

// Compare two items, for sorting
typedef int (zlistx_comparator_fn) (
    const void *item1, const void *item2);

// Callback function for reactor socket activity
typedef int (zloop_reader_fn) (
    zloop_t *loop, zsock_t *reader, void *arg);

// Callback function for reactor events (low-level)
typedef int (zloop_fn) (
    zloop_t *loop, zmq_pollitem_t *item, void *arg);

// Callback for reactor timer events
typedef int (zloop_timer_fn) (
    zloop_t *loop, int timer_id, void *arg);

// Callback function for timer event.
typedef void (ztimerset_fn) (
    int timer_id, void *arg);

// Callback function for ztrie_node to destroy node data.
typedef void (ztrie_destroy_data_fn) (
    void **data);

// CLASS: zactor
// Create a new actor passing arbitrary arguments reference.
zactor_t *
    zactor_new (zactor_fn task, void *args);

// Destroy an actor.
void
    zactor_destroy (zactor_t **self_p);

// Send a zmsg message to the actor, take ownership of the message
// and destroy when it has been sent.                             
int
    zactor_send (zactor_t *self, zmsg_t **msg_p);

// Receive a zmsg message from the actor. Returns NULL if the actor 
// was interrupted before the message could be received, or if there
// was a timeout on the actor.                                      
zmsg_t *
    zactor_recv (zactor_t *self);

// Probe the supplied object, and report if it looks like a zactor_t.
bool
    zactor_is (void *self);

// Probe the supplied reference. If it looks like a zactor_t instance,
// return the underlying libzmq actor handle; else if it looks like   
// a libzmq actor handle, return the supplied value.                  
void *
    zactor_resolve (void *self);

// Return the actor's zsock handle. Use this when you absolutely need
// to work with the zsock instance rather than the actor.            
zsock_t *
    zactor_sock (zactor_t *self);

// Self test of this class.
void
    zactor_test (bool verbose);

// CLASS: zargs
// Create a new zargs from command line arguments.
zargs_t *
    zargs_new (int argc, char **argv);

// Destroy zargs instance.
void
    zargs_destroy (zargs_t **self_p);

// Return program name (argv[0])
const char *
    zargs_progname (zargs_t *self);

// Return number of positional arguments
size_t
    zargs_arguments (zargs_t *self);

// Return first positional argument or NULL
const char *
    zargs_first (zargs_t *self);

// Return next positional argument or NULL
const char *
    zargs_next (zargs_t *self);

// Return first named parameter value, or NULL if there are no named   
// parameters, or value for which zargs_param_empty (arg) returns true.
const char *
    zargs_param_first (zargs_t *self);

// Return next named parameter value, or NULL if there are no named    
// parameters, or value for which zargs_param_empty (arg) returns true.
const char *
    zargs_param_next (zargs_t *self);

// Return current parameter name, or NULL if there are no named
// parameters.                                                 
const char *
    zargs_param_name (zargs_t *self);

// Return value of named parameter, NULL if no given parameter has
// been specified, or special value for wich zargs_param_empty () 
// returns true.                                                  
const char *
    zargs_param_lookup (zargs_t *self, const char *keys);

// Return value of named parameter(s), NULL if no given parameter has
// been specified, or special value for wich zargs_param_empty ()    
// returns true.                                                     
const char *
    zargs_param_lookupx (zargs_t *self, const char *keys, ...);

// Returns true if there are --help -h arguments
bool
    zargs_has_help (zargs_t *self);

// Returns true if parameter did not have a value
bool
    zargs_param_empty (const char *arg);

// Print an instance of zargs.
void
    zargs_print (zargs_t *self);

// Self test of this class.
void
    zargs_test (bool verbose);

// CLASS: zarmour
// Create a new zarmour
zarmour_t *
    zarmour_new (void);

// Destroy the zarmour
void
    zarmour_destroy (zarmour_t **self_p);

// Encode a stream of bytes into an armoured string. Returns the armoured
// string, or NULL if there was insufficient memory available to allocate
// a new string.                                                         
char *
    zarmour_encode (zarmour_t *self, const byte *data, size_t size);

// Decode an armoured string into a chunk. The decoded output is    
// null-terminated, so it may be treated as a string, if that's what
// it was prior to encoding.                                        
zchunk_t *
    zarmour_decode (zarmour_t *self, const char *data);

// Get the mode property.
int
    zarmour_mode (zarmour_t *self);

// Get printable string for mode.
const char *
    zarmour_mode_str (zarmour_t *self);

// Set the mode property.
void
    zarmour_set_mode (zarmour_t *self, int mode);

// Return true if padding is turned on.
bool
    zarmour_pad (zarmour_t *self);

// Turn padding on or off. Default is on.
void
    zarmour_set_pad (zarmour_t *self, bool pad);

// Get the padding character.
char
    zarmour_pad_char (zarmour_t *self);

// Set the padding character.
void
    zarmour_set_pad_char (zarmour_t *self, char pad_char);

// Return if splitting output into lines is turned on. Default is off.
bool
    zarmour_line_breaks (zarmour_t *self);

// Turn splitting output into lines on or off.
void
    zarmour_set_line_breaks (zarmour_t *self, bool line_breaks);

// Get the line length used for splitting lines.
size_t
    zarmour_line_length (zarmour_t *self);

// Set the line length used for splitting lines.
void
    zarmour_set_line_length (zarmour_t *self, size_t line_length);

// Print properties of object
void
    zarmour_print (zarmour_t *self);

// Self test of this class.
void
    zarmour_test (bool verbose);

// CLASS: zcert
// Create and initialize a new certificate in memory
zcert_t *
    zcert_new (void);

// Accepts public/secret key pair from caller
zcert_t *
    zcert_new_from (const byte *public_key, const byte *secret_key);

// Load certificate from file
zcert_t *
    zcert_load (const char *filename);

// Destroy a certificate in memory
void
    zcert_destroy (zcert_t **self_p);

// Return public part of key pair as 32-byte binary string
const byte *
    zcert_public_key (zcert_t *self);

// Return secret part of key pair as 32-byte binary string
const byte *
    zcert_secret_key (zcert_t *self);

// Return public part of key pair as Z85 armored string
const char *
    zcert_public_txt (zcert_t *self);

// Return secret part of key pair as Z85 armored string
const char *
    zcert_secret_txt (zcert_t *self);

// Set certificate metadata from formatted string.
void
    zcert_set_meta (zcert_t *self, const char *name, const char *format, ...);

// Unset certificate metadata.
void
    zcert_unset_meta (zcert_t *self, const char *name);

// Get metadata value from certificate; if the metadata value doesn't
// exist, returns NULL.                                              
const char *
    zcert_meta (zcert_t *self, const char *name);

// Get list of metadata fields from certificate. Caller is responsible for
// destroying list. Caller should not modify the values of list items.    
zlist_t *
    zcert_meta_keys (zcert_t *self);

// Save full certificate (public + secret) to file for persistent storage  
// This creates one public file and one secret file (filename + "_secret").
int
    zcert_save (zcert_t *self, const char *filename);

// Save public certificate only to file for persistent storage
int
    zcert_save_public (zcert_t *self, const char *filename);

// Save secret certificate only to file for persistent storage
int
    zcert_save_secret (zcert_t *self, const char *filename);

// Apply certificate to socket, i.e. use for CURVE security on socket.
// If certificate was loaded from public file, the secret key will be 
// undefined, and this certificate will not work successfully.        
void
    zcert_apply (zcert_t *self, void *socket);

// Return copy of certificate; if certificate is NULL or we exhausted
// heap memory, returns NULL.                                        
zcert_t *
    zcert_dup (zcert_t *self);

// Return true if two certificates have the same keys
bool
    zcert_eq (zcert_t *self, zcert_t *compare);

// Print certificate contents to stdout
void
    zcert_print (zcert_t *self);

// Self test of this class
void
    zcert_test (bool verbose);

// CLASS: zcertstore
// Create a new certificate store from a disk directory, loading and        
// indexing all certificates in that location. The directory itself may be  
// absent, and created later, or modified at any time. The certificate store
// is automatically refreshed on any zcertstore_lookup() call. If the       
// location is specified as NULL, creates a pure-memory store, which you    
// can work with by inserting certificates at runtime.                      
zcertstore_t *
    zcertstore_new (const char *location);

// Destroy a certificate store object in memory. Does not affect anything
// stored on disk.                                                       
void
    zcertstore_destroy (zcertstore_t **self_p);

// Override the default disk loader with a custom loader fn.
void
    zcertstore_set_loader (zcertstore_t *self, zcertstore_loader loader, zcertstore_destructor destructor, void *state);

// Look up certificate by public key, returns zcert_t object if found,
// else returns NULL. The public key is provided in Z85 text format.  
zcert_t *
    zcertstore_lookup (zcertstore_t *self, const char *public_key);

// Insert certificate into certificate store in memory. Note that this
// does not save the certificate to disk. To do that, use zcert_save()
// directly on the certificate. Takes ownership of zcert_t object.    
void
    zcertstore_insert (zcertstore_t *self, zcert_t **cert_p);

// Empty certificate hashtable. This wrapper exists to be friendly to bindings,
// which don't usually have access to struct internals.                        
void
    zcertstore_empty (zcertstore_t *self);

// Print list of certificates in store to logging facility
void
    zcertstore_print (zcertstore_t *self);

// Self test of this class
void
    zcertstore_test (bool verbose);

// CLASS: zchunk
// Create a new chunk of the specified size. If you specify the data, it   
// is copied into the chunk. If you do not specify the data, the chunk is  
// allocated and left empty, and you can then add data using zchunk_append.
zchunk_t *
    zchunk_new (const void *data, size_t size);

// Destroy a chunk
void
    zchunk_destroy (zchunk_t **self_p);

// Resizes chunk max_size as requested; chunk_cur size is set to zero
void
    zchunk_resize (zchunk_t *self, size_t size);

// Return chunk cur size
size_t
    zchunk_size (zchunk_t *self);

// Return chunk max size
size_t
    zchunk_max_size (zchunk_t *self);

// Return chunk data
byte *
    zchunk_data (zchunk_t *self);

// Set chunk data from user-supplied data; truncate if too large. Data may
// be null. Returns actual size of chunk                                  
size_t
    zchunk_set (zchunk_t *self, const void *data, size_t size);

// Fill chunk data from user-supplied octet
size_t
    zchunk_fill (zchunk_t *self, byte filler, size_t size);

// Append user-supplied data to chunk, return resulting chunk size. If the 
// data would exceeded the available space, it is truncated. If you want to
// grow the chunk to accommodate new data, use the zchunk_extend method.   
size_t
    zchunk_append (zchunk_t *self, const void *data, size_t size);

// Append user-supplied data to chunk, return resulting chunk size. If the
// data would exceeded the available space, the chunk grows in size.      
size_t
    zchunk_extend (zchunk_t *self, const void *data, size_t size);

// Copy as much data from 'source' into the chunk as possible; returns the  
// new size of chunk. If all data from 'source' is used, returns exhausted  
// on the source chunk. Source can be consumed as many times as needed until
// it is exhausted. If source was already exhausted, does not change chunk. 
size_t
    zchunk_consume (zchunk_t *self, zchunk_t *source);

// Returns true if the chunk was exhausted by consume methods, or if the
// chunk has a size of zero.                                            
bool
    zchunk_exhausted (zchunk_t *self);

// Read chunk from an open file descriptor
zchunk_t *
    zchunk_read (FILE *handle, size_t bytes);

// Write chunk to an open file descriptor
int
    zchunk_write (zchunk_t *self, FILE *handle);

// Try to slurp an entire file into a chunk. Will read up to maxsize of  
// the file. If maxsize is 0, will attempt to read the entire file and   
// fail with an assertion if that cannot fit into memory. Returns a new  
// chunk containing the file data, or NULL if the file could not be read.
zchunk_t *
    zchunk_slurp (const char *filename, size_t maxsize);

// Create copy of chunk, as new chunk object. Returns a fresh zchunk_t   
// object, or null if there was not enough heap memory. If chunk is null,
// returns null.                                                         
zchunk_t *
    zchunk_dup (zchunk_t *self);

// Return chunk data encoded as printable hex string. Caller must free
// string when finished with it.                                      
char *
    zchunk_strhex (zchunk_t *self);

// Return chunk data copied into freshly allocated string
// Caller must free string when finished with it.        
char *
    zchunk_strdup (zchunk_t *self);

// Return TRUE if chunk body is equal to string, excluding terminator
bool
    zchunk_streq (zchunk_t *self, const char *string);

// Transform zchunk into a zframe that can be sent in a message.
zframe_t *
    zchunk_pack (zchunk_t *self);

// Transform a zframe into a zchunk.
zchunk_t *
    zchunk_unpack (zframe_t *frame);

// Calculate SHA1 digest for chunk, using zdigest class.
const char *
    zchunk_digest (zchunk_t *self);

// Dump chunk to FILE stream, for debugging and tracing.
void
    zchunk_fprint (zchunk_t *self, FILE *file);

// Dump message to stderr, for debugging and tracing.
// See zchunk_fprint for details                     
void
    zchunk_print (zchunk_t *self);

// Probe the supplied object, and report if it looks like a zchunk_t.
bool
    zchunk_is (void *self);

// Self test of this class.
void
    zchunk_test (bool verbose);

// CLASS: zclock
// Sleep for a number of milliseconds
void
    zclock_sleep (int msecs);

// Return current system clock as milliseconds. Note that this clock can  
// jump backwards (if the system clock is changed) so is unsafe to use for
// timers and time offsets. Use zclock_mono for that instead.             
int64_t
    zclock_time (void);

// Return current monotonic clock in milliseconds. Use this when you compute
// time offsets. The monotonic clock is not affected by system changes and  
// so will never be reset backwards, unlike a system clock.                 
int64_t
    zclock_mono (void);

// Return current monotonic clock in microseconds. Use this when you compute
// time offsets. The monotonic clock is not affected by system changes and  
// so will never be reset backwards, unlike a system clock.                 
int64_t
    zclock_usecs (void);

// Return formatted date/time as fresh string. Free using zstr_free().
char *
    zclock_timestr (void);

// Self test of this class.
void
    zclock_test (bool verbose);

// CLASS: zconfig
// Create new config item
zconfig_t *
    zconfig_new (const char *name, zconfig_t *parent);

// Destroy a config item and all its children
void
    zconfig_destroy (zconfig_t **self_p);

// Load a config tree from a specified ZPL text file; returns a zconfig_t  
// reference for the root, if the file exists and is readable. Returns NULL
// if the file does not exist.                                             
zconfig_t *
    zconfig_load (const char *filename);

// Equivalent to zconfig_load, taking a format string instead of a fixed
// filename.                                                            
zconfig_t *
    zconfig_loadf (const char *format, ...);

// Return name of config item
char *
    zconfig_name (zconfig_t *self);

// Return value of config item
char *
    zconfig_value (zconfig_t *self);

// Insert or update configuration key with value
void
    zconfig_put (zconfig_t *self, const char *path, const char *value);

// Equivalent to zconfig_put, accepting a format specifier and variable
// argument list, instead of a single string value.                    
void
    zconfig_putf (zconfig_t *self, const char *path, const char *format, ...);

// Get value for config item into a string value; leading slash is optional
// and ignored.                                                            
char *
    zconfig_get (zconfig_t *self, const char *path, const char *default_value);

// Set config item name, name may be NULL
void
    zconfig_set_name (zconfig_t *self, const char *name);

// Set new value for config item. The new value may be a string, a printf  
// format, or NULL. Note that if string may possibly contain '%', or if it 
// comes from an insecure source, you must use '%s' as the format, followed
// by the string.                                                          
void
    zconfig_set_value (zconfig_t *self, const char *format, ...);

// Find our first child, if any
zconfig_t *
    zconfig_child (zconfig_t *self);

// Find our first sibling, if any
zconfig_t *
    zconfig_next (zconfig_t *self);

// Find a config item along a path; leading slash is optional and ignored.
zconfig_t *
    zconfig_locate (zconfig_t *self, const char *path);

// Locate the last config item at a specified depth
zconfig_t *
    zconfig_at_depth (zconfig_t *self, int level);

// Execute a callback for each config item in the tree; returns zero if
// successful, else -1.                                                
int
    zconfig_execute (zconfig_t *self, zconfig_fct handler, void *arg);

// Add comment to config item before saving to disk. You can add as many
// comment lines as you like. If you use a null format, all comments are
// deleted.                                                             
void
    zconfig_set_comment (zconfig_t *self, const char *format, ...);

// Return comments of config item, as zlist.
zlist_t *
    zconfig_comments (zconfig_t *self);

// Save a config tree to a specified ZPL text file, where a filename
// "-" means dump to standard output.                               
int
    zconfig_save (zconfig_t *self, const char *filename);

// Equivalent to zconfig_save, taking a format string instead of a fixed
// filename.                                                            
int
    zconfig_savef (zconfig_t *self, const char *format, ...);

// Report filename used during zconfig_load, or NULL if none
const char *
    zconfig_filename (zconfig_t *self);

// Reload config tree from same file that it was previously loaded from.
// Returns 0 if OK, -1 if there was an error (and then does not change  
// existing data).                                                      
int
    zconfig_reload (zconfig_t **self_p);

// Load a config tree from a memory chunk
zconfig_t *
    zconfig_chunk_load (zchunk_t *chunk);

// Save a config tree to a new memory chunk
zchunk_t *
    zconfig_chunk_save (zconfig_t *self);

// Load a config tree from a null-terminated string
zconfig_t *
    zconfig_str_load (const char *string);

// Save a config tree to a new null terminated string
char *
    zconfig_str_save (zconfig_t *self);

// Return true if a configuration tree was loaded from a file and that
// file has changed in since the tree was loaded.                     
bool
    zconfig_has_changed (zconfig_t *self);

// Print the config file to open stream
void
    zconfig_fprint (zconfig_t *self, FILE *file);

// Print properties of object
void
    zconfig_print (zconfig_t *self);

// Self test of this class
void
    zconfig_test (bool verbose);

// CLASS: zdigest
// Constructor - creates new digest object, which you use to build up a
// digest by repeatedly calling zdigest_update() on chunks of data.    
zdigest_t *
    zdigest_new (void);

// Destroy a digest object
void
    zdigest_destroy (zdigest_t **self_p);

// Add buffer into digest calculation
void
    zdigest_update (zdigest_t *self, const byte *buffer, size_t length);

// Return final digest hash data. If built without crypto support,
// returns NULL.                                                  
const byte *
    zdigest_data (zdigest_t *self);

// Return final digest hash size
size_t
    zdigest_size (zdigest_t *self);

// Return digest as printable hex string; caller should not modify nor   
// free this string. After calling this, you may not use zdigest_update()
// on the same digest. If built without crypto support, returns NULL.    
char *
    zdigest_string (zdigest_t *self);

// Self test of this class.
void
    zdigest_test (bool verbose);

// CLASS: zdir
// Create a new directory item that loads in the full tree of the specified
// path, optionally located under some parent path. If parent is "-", then 
// loads only the top-level directory, and does not use parent as a path.  
zdir_t *
    zdir_new (const char *path, const char *parent);

// Destroy a directory tree and all children it contains.
void
    zdir_destroy (zdir_t **self_p);

// Return directory path
const char *
    zdir_path (zdir_t *self);

// Return last modification time for directory.
time_t
    zdir_modified (zdir_t *self);

// Return total hierarchy size, in bytes of data contained in all files
// in the directory tree.                                              
off_t
    zdir_cursize (zdir_t *self);

// Return directory count
size_t
    zdir_count (zdir_t *self);

// Returns a sorted list of zfile objects; Each entry in the list is a pointer
// to a zfile_t item already allocated in the zdir tree. Do not destroy the   
// original zdir tree until you are done with this list.                      
zlist_t *
    zdir_list (zdir_t *self);

// Remove directory, optionally including all files that it contains, at  
// all levels. If force is false, will only remove the directory if empty.
// If force is true, will remove all files and all subdirectories.        
void
    zdir_remove (zdir_t *self, bool force);

// Calculate differences between two versions of a directory tree.    
// Returns a list of zdir_patch_t patches. Either older or newer may  
// be null, indicating the directory is empty/absent. If alias is set,
// generates virtual filename (minus path, plus alias).               
zlist_t *
    zdir_diff (zdir_t *older, zdir_t *newer, const char *alias);

// Return full contents of directory as a zdir_patch list.
zlist_t *
    zdir_resync (zdir_t *self, const char *alias);

// Load directory cache; returns a hash table containing the SHA-1 digests
// of every file in the tree. The cache is saved between runs in .cache.  
zhash_t *
    zdir_cache (zdir_t *self);

// Print contents of directory to open stream
void
    zdir_fprint (zdir_t *self, FILE *file, int indent);

// Print contents of directory to stdout
void
    zdir_print (zdir_t *self, int indent);

// Create a new zdir_watch actor instance:                       
//                                                               
//     zactor_t *watch = zactor_new (zdir_watch, NULL);          
//                                                               
// Destroy zdir_watch instance:                                  
//                                                               
//     zactor_destroy (&watch);                                  
//                                                               
// Enable verbose logging of commands and activity:              
//                                                               
//     zstr_send (watch, "VERBOSE");                             
//                                                               
// Subscribe to changes to a directory path:                     
//                                                               
//     zsock_send (watch, "ss", "SUBSCRIBE", "directory_path");  
//                                                               
// Unsubscribe from changes to a directory path:                 
//                                                               
//     zsock_send (watch, "ss", "UNSUBSCRIBE", "directory_path");
//                                                               
// Receive directory changes:                                    
//     zsock_recv (watch, "sp", &path, &patches);                
//                                                               
//     // Delete the received data.                              
//     free (path);                                              
//     zlist_destroy (&patches);                                 
void
    zdir_watch (zsock_t *pipe, void *unused);

// Self test of this class.
void
    zdir_test (bool verbose);

// CLASS: zdir_patch
// Create new patch
zdir_patch_t *
    zdir_patch_new (const char *path, zfile_t *file, int op, const char *alias);

// Destroy a patch
void
    zdir_patch_destroy (zdir_patch_t **self_p);

// Create copy of a patch. If the patch is null, or memory was exhausted,
// returns null.                                                         
zdir_patch_t *
    zdir_patch_dup (zdir_patch_t *self);

// Return patch file directory path
const char *
    zdir_patch_path (zdir_patch_t *self);

// Return patch file item
zfile_t *
    zdir_patch_file (zdir_patch_t *self);

// Return operation
int
    zdir_patch_op (zdir_patch_t *self);

// Return patch virtual file path
const char *
    zdir_patch_vpath (zdir_patch_t *self);

// Calculate hash digest for file (create only)
void
    zdir_patch_digest_set (zdir_patch_t *self);

// Return hash digest for patch file
const char *
    zdir_patch_digest (zdir_patch_t *self);

// Self test of this class.
void
    zdir_patch_test (bool verbose);

// CLASS: zfile
// If file exists, populates properties. CZMQ supports portable symbolic
// links, which are files with the extension ".ln". A symbolic link is a
// text file containing one line, the filename of a target file. Reading
// data from the symbolic link actually reads from the target file. Path
// may be NULL, in which case it is not used.                           
zfile_t *
    zfile_new (const char *path, const char *name);

// Destroy a file item
void
    zfile_destroy (zfile_t **self_p);

// Duplicate a file item, returns a newly constructed item. If the file
// is null, or memory was exhausted, returns null.                     
zfile_t *
    zfile_dup (zfile_t *self);

// Return file name, remove path if provided
const char *
    zfile_filename (zfile_t *self, const char *path);

// Refresh file properties from disk; this is not done automatically   
// on access methods, otherwise it is not possible to compare directory
// snapshots.                                                          
void
    zfile_restat (zfile_t *self);

// Return when the file was last modified. If you want this to reflect the
// current situation, call zfile_restat before checking this property.    
time_t
    zfile_modified (zfile_t *self);

// Return the last-known size of the file. If you want this to reflect the
// current situation, call zfile_restat before checking this property.    
off_t
    zfile_cursize (zfile_t *self);

// Return true if the file is a directory. If you want this to reflect   
// any external changes, call zfile_restat before checking this property.
bool
    zfile_is_directory (zfile_t *self);

// Return true if the file is a regular file. If you want this to reflect
// any external changes, call zfile_restat before checking this property.
bool
    zfile_is_regular (zfile_t *self);

// Return true if the file is readable by this process. If you want this to
// reflect any external changes, call zfile_restat before checking this    
// property.                                                               
bool
    zfile_is_readable (zfile_t *self);

// Return true if the file is writeable by this process. If you want this 
// to reflect any external changes, call zfile_restat before checking this
// property.                                                              
bool
    zfile_is_writeable (zfile_t *self);

// Check if file has stopped changing and can be safely processed.
// Updates the file statistics from disk at every call.           
bool
    zfile_is_stable (zfile_t *self);

// Return true if the file was changed on disk since the zfile_t object
// was created, or the last zfile_restat() call made on it.            
bool
    zfile_has_changed (zfile_t *self);

// Remove the file from disk
void
    zfile_remove (zfile_t *self);

// Open file for reading                             
// Returns 0 if OK, -1 if not found or not accessible
int
    zfile_input (zfile_t *self);

// Open file for writing, creating directory if needed               
// File is created if necessary; chunks can be written to file at any
// location. Returns 0 if OK, -1 if error.                           
int
    zfile_output (zfile_t *self);

// Read chunk from file at specified position. If this was the last chunk,
// sets the eof property. Returns a null chunk in case of error.          
zchunk_t *
    zfile_read (zfile_t *self, size_t bytes, off_t offset);

// Returns true if zfile_read() just read the last chunk in the file.
bool
    zfile_eof (zfile_t *self);

// Write chunk to file at specified position
// Return 0 if OK, else -1                  
int
    zfile_write (zfile_t *self, zchunk_t *chunk, off_t offset);

// Read next line of text from file. Returns a pointer to the text line,
// or NULL if there was nothing more to read from the file.             
const char *
    zfile_readln (zfile_t *self);

// Close file, if open
void
    zfile_close (zfile_t *self);

// Return file handle, if opened
FILE *
    zfile_handle (zfile_t *self);

// Calculate SHA1 digest for file, using zdigest class.
const char *
    zfile_digest (zfile_t *self);

// Self test of this class.
void
    zfile_test (bool verbose);

// CLASS: zframe
// Create a new frame. If size is not null, allocates the frame data
// to the specified size. If additionally, data is not null, copies 
// size octets from the specified data into the frame body.         
zframe_t *
    zframe_new (const void *data, size_t size);

// Destroy a frame
void
    zframe_destroy (zframe_t **self_p);

// Create an empty (zero-sized) frame
zframe_t *
    zframe_new_empty (void);

// Create a frame with a specified string content.
zframe_t *
    zframe_from (const char *string);

// Receive frame from socket, returns zframe_t object or NULL if the recv  
// was interrupted. Does a blocking recv, if you want to not block then use
// zpoller or zloop.                                                       
zframe_t *
    zframe_recv (void *source);

// Send a frame to a socket, destroy frame after sending.
// Return -1 on error, 0 on success.                     
int
    zframe_send (zframe_t **self_p, void *dest, int flags);

// Return number of bytes in frame data
size_t
    zframe_size (zframe_t *self);

// Return address of frame data
byte *
    zframe_data (zframe_t *self);

// Return meta data property for frame           
// Caller must free string when finished with it.
const char *
    zframe_meta (zframe_t *self, const char *property);

// Create a new frame that duplicates an existing frame. If frame is null,
// or memory was exhausted, returns null.                                 
zframe_t *
    zframe_dup (zframe_t *self);

// Return frame data encoded as printable hex string, useful for 0MQ UUIDs.
// Caller must free string when finished with it.                          
char *
    zframe_strhex (zframe_t *self);

// Return frame data copied into freshly allocated string
// Caller must free string when finished with it.        
char *
    zframe_strdup (zframe_t *self);

// Return TRUE if frame body is equal to string, excluding terminator
bool
    zframe_streq (zframe_t *self, const char *string);

// Return frame MORE indicator (1 or 0), set when reading frame from socket
// or by the zframe_set_more() method                                      
int
    zframe_more (zframe_t *self);

// Set frame MORE indicator (1 or 0). Note this is NOT used when sending
// frame to socket, you have to specify flag explicitly.                
void
    zframe_set_more (zframe_t *self, int more);

// Return frame routing ID, if the frame came from a ZMQ_SERVER socket.
// Else returns zero.                                                  
uint32_t
    zframe_routing_id (zframe_t *self);

// Set routing ID on frame. This is used if/when the frame is sent to a
// ZMQ_SERVER socket.                                                  
void
    zframe_set_routing_id (zframe_t *self, uint32_t routing_id);

// Return frame group of radio-dish pattern.
const char *
    zframe_group (zframe_t *self);

// Set group on frame. This is used if/when the frame is sent to a
// ZMQ_RADIO socket.                                              
// Return -1 on error, 0 on success.                              
int
    zframe_set_group (zframe_t *self, const char *group);

// Return TRUE if two frames have identical size and data
// If either frame is NULL, equality is always false.    
bool
    zframe_eq (zframe_t *self, zframe_t *other);

// Set new contents for frame
void
    zframe_reset (zframe_t *self, const void *data, size_t size);

// Send message to zsys log sink (may be stdout, or system facility as       
// configured by zsys_set_logstream). Prefix shows before frame, if not null.
void
    zframe_print (zframe_t *self, const char *prefix);

// Probe the supplied object, and report if it looks like a zframe_t.
bool
    zframe_is (void *self);

// Self test of this class.
void
    zframe_test (bool verbose);

// CLASS: zhash
// Create a new, empty hash container
zhash_t *
    zhash_new (void);

// Destroy a hash container and all items in it
void
    zhash_destroy (zhash_t **self_p);

// Unpack binary frame into a new hash table. Packed data must follow format
// defined by zhash_pack. Hash table is set to autofree. An empty frame     
// unpacks to an empty hash table.                                          
zhash_t *
    zhash_unpack (zframe_t *frame);

// Insert item into hash table with specified key and item.               
// If key is already present returns -1 and leaves existing item unchanged
// Returns 0 on success.                                                  
int
    zhash_insert (zhash_t *self, const char *key, void *item);

// Update item into hash table with specified key and item.            
// If key is already present, destroys old item and inserts new one.   
// Use free_fn method to ensure deallocator is properly called on item.
void
    zhash_update (zhash_t *self, const char *key, void *item);

// Remove an item specified by key from the hash table. If there was no such
// item, this function does nothing.                                        
void
    zhash_delete (zhash_t *self, const char *key);

// Return the item at the specified key, or null
void *
    zhash_lookup (zhash_t *self, const char *key);

// Reindexes an item from an old key to a new key. If there was no such
// item, does nothing. Returns 0 if successful, else -1.               
int
    zhash_rename (zhash_t *self, const char *old_key, const char *new_key);

// Set a free function for the specified hash table item. When the item is
// destroyed, the free function, if any, is called on that item.          
// Use this when hash items are dynamically allocated, to ensure that     
// you don't have memory leaks. You can pass 'free' or NULL as a free_fn. 
// Returns the item, or NULL if there is no such item.                    
void *
    zhash_freefn (zhash_t *self, const char *key, zhash_free_fn free_fn);

// Return the number of keys/items in the hash table
size_t
    zhash_size (zhash_t *self);

// Make copy of hash table; if supplied table is null, returns null.    
// Does not copy items themselves. Rebuilds new table so may be slow on 
// very large tables. NOTE: only works with item values that are strings
// since there's no other way to know how to duplicate the item value.  
zhash_t *
    zhash_dup (zhash_t *self);

// Return keys for items in table
zlist_t *
    zhash_keys (zhash_t *self);

// Simple iterator; returns first item in hash table, in no given order, 
// or NULL if the table is empty. This method is simpler to use than the 
// foreach() method, which is deprecated. To access the key for this item
// use zhash_cursor(). NOTE: do NOT modify the table while iterating.    
void *
    zhash_first (zhash_t *self);

// Simple iterator; returns next item in hash table, in no given order, 
// or NULL if the last item was already returned. Use this together with
// zhash_first() to process all items in a hash table. If you need the  
// items in sorted order, use zhash_keys() and then zlist_sort(). To    
// access the key for this item use zhash_cursor(). NOTE: do NOT modify 
// the table while iterating.                                           
void *
    zhash_next (zhash_t *self);

// After a successful first/next method, returns the key for the item that
// was returned. This is a constant string that you may not modify or     
// deallocate, and which lasts as long as the item in the hash. After an  
// unsuccessful first/next, returns NULL.                                 
const char *
    zhash_cursor (zhash_t *self);

// Add a comment to hash table before saving to disk. You can add as many   
// comment lines as you like. These comment lines are discarded when loading
// the file. If you use a null format, all comments are deleted.            
void
    zhash_comment (zhash_t *self, const char *format, ...);

// Serialize hash table to a binary frame that can be sent in a message.
// The packed format is compatible with the 'dictionary' type defined in
// http://rfc.zeromq.org/spec:35/FILEMQ, and implemented by zproto:     
//                                                                      
//    ; A list of name/value pairs                                      
//    dictionary      = dict-count *( dict-name dict-value )            
//    dict-count      = number-4                                        
//    dict-value      = longstr                                         
//    dict-name       = string                                          
//                                                                      
//    ; Strings are always length + text contents                       
//    longstr         = number-4 *VCHAR                                 
//    string          = number-1 *VCHAR                                 
//                                                                      
//    ; Numbers are unsigned integers in network byte order             
//    number-1        = 1OCTET                                          
//    number-4        = 4OCTET                                          
//                                                                      
// Comments are not included in the packed data. Item values MUST be    
// strings.                                                             
zframe_t *
    zhash_pack (zhash_t *self);

// Save hash table to a text file in name=value format. Hash values must be
// printable strings; keys may not contain '=' character. Returns 0 if OK, 
// else -1 if a file error occurred.                                       
int
    zhash_save (zhash_t *self, const char *filename);

// Load hash table from a text file in name=value format; hash table must 
// already exist. Hash values must printable strings; keys may not contain
// '=' character. Returns 0 if OK, else -1 if a file was not readable.    
int
    zhash_load (zhash_t *self, const char *filename);

// When a hash table was loaded from a file by zhash_load, this method will
// reload the file if it has been modified since, and is "stable", i.e. not
// still changing. Returns 0 if OK, -1 if there was an error reloading the 
// file.                                                                   
int
    zhash_refresh (zhash_t *self);

// Set hash for automatic value destruction. Note that this assumes that
// values are NULL-terminated strings. Do not use with different types. 
void
    zhash_autofree (zhash_t *self);

// Self test of this class.
void
    zhash_test (bool verbose);

// CLASS: zhashx
// Create a new, empty hash container
zhashx_t *
    zhashx_new (void);

// Destroy a hash container and all items in it
void
    zhashx_destroy (zhashx_t **self_p);

// Unpack binary frame into a new hash table. Packed data must follow format
// defined by zhashx_pack. Hash table is set to autofree. An empty frame    
// unpacks to an empty hash table.                                          
zhashx_t *
    zhashx_unpack (zframe_t *frame);

// Same as unpack but uses a user-defined deserializer function to convert
// a longstr back into item format.                                       
zhashx_t *
    zhashx_unpack_own (zframe_t *frame, zhashx_deserializer_fn deserializer);

// Insert item into hash table with specified key and item.               
// If key is already present returns -1 and leaves existing item unchanged
// Returns 0 on success.                                                  
int
    zhashx_insert (zhashx_t *self, const void *key, void *item);

// Update or insert item into hash table with specified key and item. If the
// key is already present, destroys old item and inserts new one. If you set
// a container item destructor, this is called on the old value. If the key 
// was not already present, inserts a new item. Sets the hash cursor to the 
// new item.                                                                
void
    zhashx_update (zhashx_t *self, const void *key, void *item);

// Remove an item specified by key from the hash table. If there was no such
// item, this function does nothing.                                        
void
    zhashx_delete (zhashx_t *self, const void *key);

// Delete all items from the hash table. If the key destructor is  
// set, calls it on every key. If the item destructor is set, calls
// it on every item.                                               
void
    zhashx_purge (zhashx_t *self);

// Return the item at the specified key, or null
void *
    zhashx_lookup (zhashx_t *self, const void *key);

// Reindexes an item from an old key to a new key. If there was no such
// item, does nothing. Returns 0 if successful, else -1.               
int
    zhashx_rename (zhashx_t *self, const void *old_key, const void *new_key);

// Set a free function for the specified hash table item. When the item is
// destroyed, the free function, if any, is called on that item.          
// Use this when hash items are dynamically allocated, to ensure that     
// you don't have memory leaks. You can pass 'free' or NULL as a free_fn. 
// Returns the item, or NULL if there is no such item.                    
void *
    zhashx_freefn (zhashx_t *self, const void *key, zhashx_free_fn free_fn);

// Return the number of keys/items in the hash table
size_t
    zhashx_size (zhashx_t *self);

// Return a zlistx_t containing the keys for the items in the       
// table. Uses the key_duplicator to duplicate all keys and sets the
// key_destructor as destructor for the list.                       
zlistx_t *
    zhashx_keys (zhashx_t *self);

// Return a zlistx_t containing the values for the items in the  
// table. Uses the duplicator to duplicate all items and sets the
// destructor as destructor for the list.                        
zlistx_t *
    zhashx_values (zhashx_t *self);

// Simple iterator; returns first item in hash table, in no given order, 
// or NULL if the table is empty. This method is simpler to use than the 
// foreach() method, which is deprecated. To access the key for this item
// use zhashx_cursor(). NOTE: do NOT modify the table while iterating.   
void *
    zhashx_first (zhashx_t *self);

// Simple iterator; returns next item in hash table, in no given order, 
// or NULL if the last item was already returned. Use this together with
// zhashx_first() to process all items in a hash table. If you need the 
// items in sorted order, use zhashx_keys() and then zlistx_sort(). To  
// access the key for this item use zhashx_cursor(). NOTE: do NOT modify
// the table while iterating.                                           
void *
    zhashx_next (zhashx_t *self);

// After a successful first/next method, returns the key for the item that
// was returned. This is a constant string that you may not modify or     
// deallocate, and which lasts as long as the item in the hash. After an  
// unsuccessful first/next, returns NULL.                                 
const void *
    zhashx_cursor (zhashx_t *self);

// Add a comment to hash table before saving to disk. You can add as many   
// comment lines as you like. These comment lines are discarded when loading
// the file. If you use a null format, all comments are deleted.            
void
    zhashx_comment (zhashx_t *self, const char *format, ...);

// Save hash table to a text file in name=value format. Hash values must be
// printable strings; keys may not contain '=' character. Returns 0 if OK, 
// else -1 if a file error occurred.                                       
int
    zhashx_save (zhashx_t *self, const char *filename);

// Load hash table from a text file in name=value format; hash table must 
// already exist. Hash values must printable strings; keys may not contain
// '=' character. Returns 0 if OK, else -1 if a file was not readable.    
int
    zhashx_load (zhashx_t *self, const char *filename);

// When a hash table was loaded from a file by zhashx_load, this method will
// reload the file if it has been modified since, and is "stable", i.e. not 
// still changing. Returns 0 if OK, -1 if there was an error reloading the  
// file.                                                                    
int
    zhashx_refresh (zhashx_t *self);

// Serialize hash table to a binary frame that can be sent in a message.
// The packed format is compatible with the 'dictionary' type defined in
// http://rfc.zeromq.org/spec:35/FILEMQ, and implemented by zproto:     
//                                                                      
//    ; A list of name/value pairs                                      
//    dictionary      = dict-count *( dict-name dict-value )            
//    dict-count      = number-4                                        
//    dict-value      = longstr                                         
//    dict-name       = string                                          
//                                                                      
//    ; Strings are always length + text contents                       
//    longstr         = number-4 *VCHAR                                 
//    string          = number-1 *VCHAR                                 
//                                                                      
//    ; Numbers are unsigned integers in network byte order             
//    number-1        = 1OCTET                                          
//    number-4        = 4OCTET                                          
//                                                                      
// Comments are not included in the packed data. Item values MUST be    
// strings.                                                             
zframe_t *
    zhashx_pack (zhashx_t *self);

// Same as pack but uses a user-defined serializer function to convert items
// into longstr.                                                            
zframe_t *
    zhashx_pack_own (zhashx_t *self, zhashx_serializer_fn serializer);

// Make a copy of the list; items are duplicated if you set a duplicator 
// for the list, otherwise not. Copying a null reference returns a null  
// reference. Note that this method's behavior changed slightly for CZMQ 
// v3.x, as it does not set nor respect autofree. It does however let you
// duplicate any hash table safely. The old behavior is in zhashx_dup_v2.
zhashx_t *
    zhashx_dup (zhashx_t *self);

// Set a user-defined deallocator for hash items; by default items are not
// freed when the hash is destroyed.                                      
void
    zhashx_set_destructor (zhashx_t *self, zhashx_destructor_fn destructor);

// Set a user-defined duplicator for hash items; by default items are not
// copied when the hash is duplicated.                                   
void
    zhashx_set_duplicator (zhashx_t *self, zhashx_duplicator_fn duplicator);

// Set a user-defined deallocator for keys; by default keys are freed
// when the hash is destroyed using free().                          
void
    zhashx_set_key_destructor (zhashx_t *self, zhashx_destructor_fn destructor);

// Set a user-defined duplicator for keys; by default keys are duplicated
// using strdup.                                                         
void
    zhashx_set_key_duplicator (zhashx_t *self, zhashx_duplicator_fn duplicator);

// Set a user-defined comparator for keys; by default keys are
// compared using strcmp.                                     
void
    zhashx_set_key_comparator (zhashx_t *self, zhashx_comparator_fn comparator);

// Set a user-defined comparator for keys; by default keys are
// compared using strcmp.                                     
void
    zhashx_set_key_hasher (zhashx_t *self, zhashx_hash_fn hasher);

// Make copy of hash table; if supplied table is null, returns null.    
// Does not copy items themselves. Rebuilds new table so may be slow on 
// very large tables. NOTE: only works with item values that are strings
// since there's no other way to know how to duplicate the item value.  
zhashx_t *
    zhashx_dup_v2 (zhashx_t *self);

// Self test of this class.
void
    zhashx_test (bool verbose);

// CLASS: ziflist
// Get a list of network interfaces currently defined on the system
ziflist_t *
    ziflist_new (void);

// Destroy a ziflist instance
void
    ziflist_destroy (ziflist_t **self_p);

// Reload network interfaces from system
void
    ziflist_reload (ziflist_t *self);

// Return the number of network interfaces on system
size_t
    ziflist_size (ziflist_t *self);

// Get first network interface, return NULL if there are none
const char *
    ziflist_first (ziflist_t *self);

// Get next network interface, return NULL if we hit the last one
const char *
    ziflist_next (ziflist_t *self);

// Return the current interface IP address as a printable string
const char *
    ziflist_address (ziflist_t *self);

// Return the current interface broadcast address as a printable string
const char *
    ziflist_broadcast (ziflist_t *self);

// Return the current interface network mask as a printable string
const char *
    ziflist_netmask (ziflist_t *self);

// Return the list of interfaces.
void
    ziflist_print (ziflist_t *self);

// Get a list of network interfaces currently defined on the system
// Includes IPv6 interfaces                                        
ziflist_t *
    ziflist_new_ipv6 (void);

// Reload network interfaces from system, including IPv6
void
    ziflist_reload_ipv6 (ziflist_t *self);

// Return true if the current interface uses IPv6
bool
    ziflist_is_ipv6 (ziflist_t *self);

// Self test of this class.
void
    ziflist_test (bool verbose);

// CLASS: zlist
// Create a new list container
zlist_t *
    zlist_new (void);

// Destroy a list container
void
    zlist_destroy (zlist_t **self_p);

// Return the item at the head of list. If the list is empty, returns NULL.
// Leaves cursor pointing at the head item, or NULL if the list is empty.  
void *
    zlist_first (zlist_t *self);

// Return the next item. If the list is empty, returns NULL. To move to
// the start of the list call zlist_first (). Advances the cursor.     
void *
    zlist_next (zlist_t *self);

// Return the item at the tail of list. If the list is empty, returns NULL.
// Leaves cursor pointing at the tail item, or NULL if the list is empty.  
void *
    zlist_last (zlist_t *self);

// Return first item in the list, or null, leaves the cursor
void *
    zlist_head (zlist_t *self);

// Return last item in the list, or null, leaves the cursor
void *
    zlist_tail (zlist_t *self);

// Return the current item of list. If the list is empty, returns NULL.     
// Leaves cursor pointing at the current item, or NULL if the list is empty.
void *
    zlist_item (zlist_t *self);

// Append an item to the end of the list, return 0 if OK or -1 if this  
// failed for some reason (out of memory). Note that if a duplicator has
// been set, this method will also duplicate the item.                  
int
    zlist_append (zlist_t *self, void *item);

// Push an item to the start of the list, return 0 if OK or -1 if this  
// failed for some reason (out of memory). Note that if a duplicator has
// been set, this method will also duplicate the item.                  
int
    zlist_push (zlist_t *self, void *item);

// Pop the item off the start of the list, if any
void *
    zlist_pop (zlist_t *self);

// Checks if an item already is present. Uses compare method to determine if 
// items are equal. If the compare method is NULL the check will only compare
// pointers. Returns true if item is present else false.                     
bool
    zlist_exists (zlist_t *self, void *item);

// Remove the specified item from the list if present
void
    zlist_remove (zlist_t *self, void *item);

// Make a copy of list. If the list has autofree set, the copied list will  
// duplicate all items, which must be strings. Otherwise, the list will hold
// pointers back to the items in the original list. If list is null, returns
// NULL.                                                                    
zlist_t *
    zlist_dup (zlist_t *self);

// Purge all items from list
void
    zlist_purge (zlist_t *self);

// Return number of items in the list
size_t
    zlist_size (zlist_t *self);

// Sort the list. If the compare function is null, sorts the list by     
// ascending key value using a straight ASCII comparison. If you specify 
// a compare function, this decides how items are sorted. The sort is not
// stable, so may reorder items with the same keys. The algorithm used is
// combsort, a compromise between performance and simplicity.            
void
    zlist_sort (zlist_t *self, zlist_compare_fn compare);

// Set list for automatic item destruction; item values MUST be strings. 
// By default a list item refers to a value held elsewhere. When you set 
// this, each time you append or push a list item, zlist will take a copy
// of the string value. Then, when you destroy the list, it will free all
// item values automatically. If you use any other technique to allocate 
// list values, you must free them explicitly before destroying the list.
// The usual technique is to pop list items and destroy them, until the  
// list is empty.                                                        
void
    zlist_autofree (zlist_t *self);

// Sets a compare function for this list. The function compares two items.
// It returns an integer less than, equal to, or greater than zero if the 
// first item is found, respectively, to be less than, to match, or be    
// greater than the second item.                                          
// This function is used for sorting, removal and exists checking.        
void
    zlist_comparefn (zlist_t *self, zlist_compare_fn fn);

// Set a free function for the specified list item. When the item is     
// destroyed, the free function, if any, is called on that item.         
// Use this when list items are dynamically allocated, to ensure that    
// you don't have memory leaks. You can pass 'free' or NULL as a free_fn.
// Returns the item, or NULL if there is no such item.                   
void *
    zlist_freefn (zlist_t *self, void *item, zlist_free_fn fn, bool at_tail);

// Self test of this class.
void
    zlist_test (bool verbose);

// CLASS: zlistx
// Create a new, empty list.
zlistx_t *
    zlistx_new (void);

// Destroy a list. If an item destructor was specified, all items in the
// list are automatically destroyed as well.                            
void
    zlistx_destroy (zlistx_t **self_p);

// Add an item to the head of the list. Calls the item duplicator, if any,
// on the item. Resets cursor to list head. Returns an item handle on     
// success, NULL if memory was exhausted.                                 
void *
    zlistx_add_start (zlistx_t *self, void *item);

// Add an item to the tail of the list. Calls the item duplicator, if any,
// on the item. Resets cursor to list head. Returns an item handle on     
// success, NULL if memory was exhausted.                                 
void *
    zlistx_add_end (zlistx_t *self, void *item);

// Return the number of items in the list
size_t
    zlistx_size (zlistx_t *self);

// Return first item in the list, or null, leaves the cursor
void *
    zlistx_head (zlistx_t *self);

// Return last item in the list, or null, leaves the cursor
void *
    zlistx_tail (zlistx_t *self);

// Return the item at the head of list. If the list is empty, returns NULL.
// Leaves cursor pointing at the head item, or NULL if the list is empty.  
void *
    zlistx_first (zlistx_t *self);

// Return the next item. At the end of the list (or in an empty list),     
// returns NULL. Use repeated zlistx_next () calls to work through the list
// from zlistx_first (). First time, acts as zlistx_first().               
void *
    zlistx_next (zlistx_t *self);

// Return the previous item. At the start of the list (or in an empty list),
// returns NULL. Use repeated zlistx_prev () calls to work through the list 
// backwards from zlistx_last (). First time, acts as zlistx_last().        
void *
    zlistx_prev (zlistx_t *self);

// Return the item at the tail of list. If the list is empty, returns NULL.
// Leaves cursor pointing at the tail item, or NULL if the list is empty.  
void *
    zlistx_last (zlistx_t *self);

// Returns the value of the item at the cursor, or NULL if the cursor is
// not pointing to an item.                                             
void *
    zlistx_item (zlistx_t *self);

// Returns the handle of the item at the cursor, or NULL if the cursor is
// not pointing to an item.                                              
void *
    zlistx_cursor (zlistx_t *self);

// Returns the item associated with the given list handle, or NULL if passed     
// in handle is NULL. Asserts that the passed in handle points to a list element.
void *
    zlistx_handle_item (void *handle);

// Find an item in the list, searching from the start. Uses the item     
// comparator, if any, else compares item values directly. Returns the   
// item handle found, or NULL. Sets the cursor to the found item, if any.
void *
    zlistx_find (zlistx_t *self, void *item);

// Detach an item from the list, using its handle. The item is not modified, 
// and the caller is responsible for destroying it if necessary. If handle is
// null, detaches the first item on the list. Returns item that was detached,
// or null if none was. If cursor was at item, moves cursor to previous item,
// so you can detach items while iterating forwards through a list.          
void *
    zlistx_detach (zlistx_t *self, void *handle);

// Detach item at the cursor, if any, from the list. The item is not modified,
// and the caller is responsible for destroying it as necessary. Returns item 
// that was detached, or null if none was. Moves cursor to previous item, so  
// you can detach items while iterating forwards through a list.              
void *
    zlistx_detach_cur (zlistx_t *self);

// Delete an item, using its handle. Calls the item destructor is any is 
// set. If handle is null, deletes the first item on the list. Returns 0 
// if an item was deleted, -1 if not. If cursor was at item, moves cursor
// to previous item, so you can delete items while iterating forwards    
// through a list.                                                       
int
    zlistx_delete (zlistx_t *self, void *handle);

// Move an item to the start of the list, via its handle.
void
    zlistx_move_start (zlistx_t *self, void *handle);

// Move an item to the end of the list, via its handle.
void
    zlistx_move_end (zlistx_t *self, void *handle);

// Remove all items from the list, and destroy them if the item destructor
// is set.                                                                
void
    zlistx_purge (zlistx_t *self);

// Sort the list. If an item comparator was set, calls that to compare    
// items, otherwise compares on item value. The sort is not stable, so may
// reorder equal items.                                                   
void
    zlistx_sort (zlistx_t *self);

// Create a new node and insert it into a sorted list. Calls the item        
// duplicator, if any, on the item. If low_value is true, starts searching   
// from the start of the list, otherwise searches from the end. Use the item 
// comparator, if any, to find where to place the new node. Returns a handle 
// to the new node, or NULL if memory was exhausted. Resets the cursor to the
// list head.                                                                
void *
    zlistx_insert (zlistx_t *self, void *item, bool low_value);

// Move an item, specified by handle, into position in a sorted list. Uses 
// the item comparator, if any, to determine the new location. If low_value
// is true, starts searching from the start of the list, otherwise searches
// from the end.                                                           
void
    zlistx_reorder (zlistx_t *self, void *handle, bool low_value);

// Make a copy of the list; items are duplicated if you set a duplicator
// for the list, otherwise not. Copying a null reference returns a null 
// reference.                                                           
zlistx_t *
    zlistx_dup (zlistx_t *self);

// Set a user-defined deallocator for list items; by default items are not
// freed when the list is destroyed.                                      
void
    zlistx_set_destructor (zlistx_t *self, zlistx_destructor_fn destructor);

// Set a user-defined duplicator for list items; by default items are not
// copied when the list is duplicated.                                   
void
    zlistx_set_duplicator (zlistx_t *self, zlistx_duplicator_fn duplicator);

// Set a user-defined comparator for zlistx_find and zlistx_sort; the method 
// must return -1, 0, or 1 depending on whether item1 is less than, equal to,
// or greater than, item2.                                                   
void
    zlistx_set_comparator (zlistx_t *self, zlistx_comparator_fn comparator);

// Self test of this class.
void
    zlistx_test (bool verbose);

// CLASS: zloop
// Create a new zloop reactor
zloop_t *
    zloop_new (void);

// Destroy a reactor
void
    zloop_destroy (zloop_t **self_p);

// Register socket reader with the reactor. When the reader has messages, 
// the reactor will call the handler, passing the arg. Returns 0 if OK, -1
// if there was an error. If you register the same socket more than once, 
// each instance will invoke its corresponding handler.                   
int
    zloop_reader (zloop_t *self, zsock_t *sock, zloop_reader_fn handler, void *arg);

// Cancel a socket reader from the reactor. If multiple readers exist for
// same socket, cancels ALL of them.                                     
void
    zloop_reader_end (zloop_t *self, zsock_t *sock);

// Configure a registered reader to ignore errors. If you do not set this,
// then readers that have errors are removed from the reactor silently.   
void
    zloop_reader_set_tolerant (zloop_t *self, zsock_t *sock);

// Register low-level libzmq pollitem with the reactor. When the pollitem  
// is ready, will call the handler, passing the arg. Returns 0 if OK, -1   
// if there was an error. If you register the pollitem more than once, each
// instance will invoke its corresponding handler. A pollitem with         
// socket=NULL and fd=0 means 'poll on FD zero'.                           
int
    zloop_poller (zloop_t *self, zmq_pollitem_t *item, zloop_fn handler, void *arg);

// Cancel a pollitem from the reactor, specified by socket or FD. If both
// are specified, uses only socket. If multiple poll items exist for same
// socket/FD, cancels ALL of them.                                       
void
    zloop_poller_end (zloop_t *self, zmq_pollitem_t *item);

// Configure a registered poller to ignore errors. If you do not set this,
// then poller that have errors are removed from the reactor silently.    
void
    zloop_poller_set_tolerant (zloop_t *self, zmq_pollitem_t *item);

// Register a timer that expires after some delay and repeats some number of
// times. At each expiry, will call the handler, passing the arg. To run a  
// timer forever, use 0 times. Returns a timer_id that is used to cancel the
// timer in the future. Returns -1 if there was an error.                   
int
    zloop_timer (zloop_t *self, size_t delay, size_t times, zloop_timer_fn handler, void *arg);

// Cancel a specific timer identified by a specific timer_id (as returned by
// zloop_timer).                                                            
int
    zloop_timer_end (zloop_t *self, int timer_id);

// Register a ticket timer. Ticket timers are very fast in the case where   
// you use a lot of timers (thousands), and frequently remove and add them. 
// The main use case is expiry timers for servers that handle many clients, 
// and which reset the expiry timer for each message received from a client.
// Whereas normal timers perform poorly as the number of clients grows, the 
// cost of ticket timers is constant, no matter the number of clients. You  
// must set the ticket delay using zloop_set_ticket_delay before creating a 
// ticket. Returns a handle to the timer that you should use in             
// zloop_ticket_reset and zloop_ticket_delete.                              
void *
    zloop_ticket (zloop_t *self, zloop_timer_fn handler, void *arg);

// Reset a ticket timer, which moves it to the end of the ticket list and
// resets its execution time. This is a very fast operation.             
void
    zloop_ticket_reset (zloop_t *self, void *handle);

// Delete a ticket timer. We do not actually delete the ticket here, as    
// other code may still refer to the ticket. We mark as deleted, and remove
// later and safely.                                                       
void
    zloop_ticket_delete (zloop_t *self, void *handle);

// Set the ticket delay, which applies to all tickets. If you lower the   
// delay and there are already tickets created, the results are undefined.
void
    zloop_set_ticket_delay (zloop_t *self, size_t ticket_delay);

// Set hard limit on number of timers allowed. Setting more than a small  
// number of timers (10-100) can have a dramatic impact on the performance
// of the reactor. For high-volume cases, use ticket timers. If the hard  
// limit is reached, the reactor stops creating new timers and logs an    
// error.                                                                 
void
    zloop_set_max_timers (zloop_t *self, size_t max_timers);

// Set verbose tracing of reactor on/off. The default verbose setting is
// off (false).                                                         
void
    zloop_set_verbose (zloop_t *self, bool verbose);

// By default the reactor stops if the process receives a SIGINT or SIGTERM 
// signal. This makes it impossible to shut-down message based architectures
// like zactors. This method lets you switch off break handling. The default
// nonstop setting is off (false).                                          
void
    zloop_set_nonstop (zloop_t *self, bool nonstop);

// Start the reactor. Takes control of the thread and returns when the 0MQ  
// context is terminated or the process is interrupted, or any event handler
// returns -1. Event handlers may register new sockets and timers, and      
// cancel sockets. Returns 0 if interrupted, -1 if canceled by a handler.   
int
    zloop_start (zloop_t *self);

// Self test of this class.
void
    zloop_test (bool verbose);

// CLASS: zmsg
// Create a new empty message object
zmsg_t *
    zmsg_new (void);

// Destroy a message object and all frames it contains
void
    zmsg_destroy (zmsg_t **self_p);

// Receive message from socket, returns zmsg_t object or NULL if the recv   
// was interrupted. Does a blocking recv. If you want to not block then use 
// the zloop class or zmsg_recv_nowait or zmq_poll to check for socket input
// before receiving.                                                        
zmsg_t *
    zmsg_recv (void *source);

// Load/append an open file into new message, return the message.
// Returns NULL if the message could not be loaded.              
zmsg_t *
    zmsg_load (FILE *file);

// Decodes a serialized message frame created by zmsg_encode () and returns
// a new zmsg_t object. Returns NULL if the frame was badly formatted or   
// there was insufficient memory to work.                                  
zmsg_t *
    zmsg_decode (zframe_t *frame);

// Generate a signal message encoding the given status. A signal is a short
// message carrying a 1-byte success/failure code (by convention, 0 means  
// OK). Signals are encoded to be distinguishable from "normal" messages.  
zmsg_t *
    zmsg_new_signal (byte status);

// Send message to destination socket, and destroy the message after sending
// it successfully. If the message has no frames, sends nothing but destroys
// the message anyhow. Nullifies the caller's reference to the message (as  
// it is a destructor).                                                     
int
    zmsg_send (zmsg_t **self_p, void *dest);

// Send message to destination socket as part of a multipart sequence, and 
// destroy the message after sending it successfully. Note that after a    
// zmsg_sendm, you must call zmsg_send or another method that sends a final
// message part. If the message has no frames, sends nothing but destroys  
// the message anyhow. Nullifies the caller's reference to the message (as 
// it is a destructor).                                                    
int
    zmsg_sendm (zmsg_t **self_p, void *dest);

// Return size of message, i.e. number of frames (0 or more).
size_t
    zmsg_size (zmsg_t *self);

// Return total size of all frames in message.
size_t
    zmsg_content_size (zmsg_t *self);

// Return message routing ID, if the message came from a ZMQ_SERVER socket.
// Else returns zero.                                                      
uint32_t
    zmsg_routing_id (zmsg_t *self);

// Set routing ID on message. This is used if/when the message is sent to a
// ZMQ_SERVER socket.                                                      
void
    zmsg_set_routing_id (zmsg_t *self, uint32_t routing_id);

// Push frame to the front of the message, i.e. before all other frames.  
// Message takes ownership of frame, will destroy it when message is sent.
// Returns 0 on success, -1 on error. Deprecates zmsg_push, which did not 
// nullify the caller's frame reference.                                  
int
    zmsg_prepend (zmsg_t *self, zframe_t **frame_p);

// Add frame to the end of the message, i.e. after all other frames.      
// Message takes ownership of frame, will destroy it when message is sent.
// Returns 0 on success. Deprecates zmsg_add, which did not nullify the   
// caller's frame reference.                                              
int
    zmsg_append (zmsg_t *self, zframe_t **frame_p);

// Remove first frame from message, if any. Returns frame, or NULL.
zframe_t *
    zmsg_pop (zmsg_t *self);

// Push block of memory to front of message, as a new frame.
// Returns 0 on success, -1 on error.                       
int
    zmsg_pushmem (zmsg_t *self, const void *data, size_t size);

// Add block of memory to the end of the message, as a new frame.
// Returns 0 on success, -1 on error.                            
int
    zmsg_addmem (zmsg_t *self, const void *data, size_t size);

// Push string as new frame to front of message.
// Returns 0 on success, -1 on error.           
int
    zmsg_pushstr (zmsg_t *self, const char *string);

// Push string as new frame to end of message.
// Returns 0 on success, -1 on error.         
int
    zmsg_addstr (zmsg_t *self, const char *string);

// Push formatted string as new frame to front of message.
// Returns 0 on success, -1 on error.                     
int
    zmsg_pushstrf (zmsg_t *self, const char *format, ...);

// Push formatted string as new frame to end of message.
// Returns 0 on success, -1 on error.                   
int
    zmsg_addstrf (zmsg_t *self, const char *format, ...);

// Pop frame off front of message, return as fresh string. If there were
// no more frames in the message, returns NULL.                         
char *
    zmsg_popstr (zmsg_t *self);

// Push encoded message as a new frame. Message takes ownership of    
// submessage, so the original is destroyed in this call. Returns 0 on
// success, -1 on error.                                              
int
    zmsg_addmsg (zmsg_t *self, zmsg_t **msg_p);

// Remove first submessage from message, if any. Returns zmsg_t, or NULL if
// decoding was not successful.                                            
zmsg_t *
    zmsg_popmsg (zmsg_t *self);

// Remove specified frame from list, if present. Does not destroy frame.
void
    zmsg_remove (zmsg_t *self, zframe_t *frame);

// Set cursor to first frame in message. Returns frame, or NULL, if the
// message is empty. Use this to navigate the frames as a list.        
zframe_t *
    zmsg_first (zmsg_t *self);

// Return the next frame. If there are no more frames, returns NULL. To move
// to the first frame call zmsg_first(). Advances the cursor.               
zframe_t *
    zmsg_next (zmsg_t *self);

// Return the last frame. If there are no frames, returns NULL.
zframe_t *
    zmsg_last (zmsg_t *self);

// Save message to an open file, return 0 if OK, else -1. The message is  
// saved as a series of frames, each with length and data. Note that the  
// file is NOT guaranteed to be portable between operating systems, not   
// versions of CZMQ. The file format is at present undocumented and liable
// to arbitrary change.                                                   
int
    zmsg_save (zmsg_t *self, FILE *file);

// Serialize multipart message to a single message frame. Use this method
// to send structured messages across transports that do not support     
// multipart data. Allocates and returns a new frame containing the      
// serialized message. To decode a serialized message frame, use         
// zmsg_decode ().                                                       
zframe_t *
    zmsg_encode (zmsg_t *self);

// Create copy of message, as new message object. Returns a fresh zmsg_t
// object. If message is null, or memory was exhausted, returns null.   
zmsg_t *
    zmsg_dup (zmsg_t *self);

// Send message to zsys log sink (may be stdout, or system facility as
// configured by zsys_set_logstream).                                 
void
    zmsg_print (zmsg_t *self);

// Return true if the two messages have the same number of frames and each  
// frame in the first message is identical to the corresponding frame in the
// other message. As with zframe_eq, return false if either message is NULL.
bool
    zmsg_eq (zmsg_t *self, zmsg_t *other);

// Return signal value, 0 or greater, if message is a signal, -1 if not.
int
    zmsg_signal (zmsg_t *self);

// Probe the supplied object, and report if it looks like a zmsg_t.
bool
    zmsg_is (void *self);

// Self test of this class.
void
    zmsg_test (bool verbose);

// CLASS: zpoller
// Create new poller, specifying zero or more readers. The list of 
// readers ends in a NULL. Each reader can be a zsock_t instance, a
// zactor_t instance, a libzmq socket (void *), or a file handle.  
zpoller_t *
    zpoller_new (void *reader, ...);

// Destroy a poller
void
    zpoller_destroy (zpoller_t **self_p);

// Add a reader to be polled. Returns 0 if OK, -1 on failure. The reader may
// be a libzmq void * socket, a zsock_t instance, or a zactor_t instance.   
int
    zpoller_add (zpoller_t *self, void *reader);

// Remove a reader from the poller; returns 0 if OK, -1 on failure. The reader
// must have been passed during construction, or in an zpoller_add () call.   
int
    zpoller_remove (zpoller_t *self, void *reader);

// By default the poller stops if the process receives a SIGINT or SIGTERM  
// signal. This makes it impossible to shut-down message based architectures
// like zactors. This method lets you switch off break handling. The default
// nonstop setting is off (false).                                          
void
    zpoller_set_nonstop (zpoller_t *self, bool nonstop);

// Poll the registered readers for I/O, return first reader that has input.  
// The reader will be a libzmq void * socket, or a zsock_t or zactor_t       
// instance as specified in zpoller_new/zpoller_add. The timeout should be   
// zero or greater, or -1 to wait indefinitely. Socket priority is defined   
// by their order in the poll list. If you need a balanced poll, use the low 
// level zmq_poll method directly. If the poll call was interrupted (SIGINT),
// or the ZMQ context was destroyed, or the timeout expired, returns NULL.   
// You can test the actual exit condition by calling zpoller_expired () and  
// zpoller_terminated (). The timeout is in msec.                            
void *
    zpoller_wait (zpoller_t *self, int timeout);

// Return true if the last zpoller_wait () call ended because the timeout
// expired, without any error.                                           
bool
    zpoller_expired (zpoller_t *self);

// Return true if the last zpoller_wait () call ended because the process
// was interrupted, or the parent context was destroyed.                 
bool
    zpoller_terminated (zpoller_t *self);

// Self test of this class.
void
    zpoller_test (bool verbose);

// CLASS: zproc
// Create a new zproc.                                        
// NOTE: On Windows and with libzmq3 and libzmq2 this function
// returns NULL. Code needs to be ported there.               
zproc_t *
    zproc_new (void);

// Destroy zproc, wait until process ends.
void
    zproc_destroy (zproc_t **self_p);

// Setup the command line arguments, the first item must be an (absolute) filename
// to run.                                                                        
void
    zproc_set_args (zproc_t *self, zlistx_t *args);

// Setup the environment variables for the process.
void
    zproc_set_env (zproc_t *self, zhashx_t *args);

// Connects process stdin with a readable ('>', connect) zeromq socket. If
// socket argument is NULL, zproc creates own managed pair of inproc      
// sockets.  The writable one is then accessbile via zproc_stdin method.  
void
    zproc_set_stdin (zproc_t *self, void *socket);

// Connects process stdout with a writable ('@', bind) zeromq socket. If 
// socket argument is NULL, zproc creates own managed pair of inproc     
// sockets.  The readable one is then accessbile via zproc_stdout method.
void
    zproc_set_stdout (zproc_t *self, void *socket);

// Connects process stderr with a writable ('@', bind) zeromq socket. If 
// socket argument is NULL, zproc creates own managed pair of inproc     
// sockets.  The readable one is then accessbile via zproc_stderr method.
void
    zproc_set_stderr (zproc_t *self, void *socket);

// Return subprocess stdin writable socket. NULL for
// not initialized or external sockets.             
void *
    zproc_stdin (zproc_t *self);

// Return subprocess stdout readable socket. NULL for
// not initialized or external sockets.              
void *
    zproc_stdout (zproc_t *self);

// Return subprocess stderr readable socket. NULL for
// not initialized or external sockets.              
void *
    zproc_stderr (zproc_t *self);

// Starts the process.
int
    zproc_run (zproc_t *self);

// process exit code
int
    zproc_returncode (zproc_t *self);

// PID of the process
int
    zproc_pid (zproc_t *self);

// return true if process is running, false if not yet started or finished
bool
    zproc_running (zproc_t *self);

// wait or poll process status, return return code
int
    zproc_wait (zproc_t *self, bool hang);

// return internal actor, usefull for the polling if process died
void *
    zproc_actor (zproc_t *self);

// send a signal to the subprocess
void
    zproc_kill (zproc_t *self, int signal);

// set verbose mode
void
    zproc_set_verbose (zproc_t *self, bool verbose);

// Returns CZMQ version as a single 6-digit integer encoding the major
// version (x 10000), the minor version (x 100) and the patch.        
int
    zproc_czmq_version (void);

// Returns true if the process received a SIGINT or SIGTERM signal.
// It is good practice to use this method to exit any infinite loop
// processing messages.                                            
bool
    zproc_interrupted (void);

// Returns true if the underlying libzmq supports CURVE security.
bool
    zproc_has_curve (void);

// Return current host name, for use in public tcp:// endpoints.
// If the host name is not resolvable, returns NULL.            
char *
    zproc_hostname (void);

// Move the current process into the background. The precise effect     
// depends on the operating system. On POSIX boxes, moves to a specified
// working directory (if specified), closes all file handles, reopens   
// stdin, stdout, and stderr to the null device, and sets the process to
// ignore SIGHUP. On Windows, does nothing. Returns 0 if OK, -1 if there
// was an error.                                                        
void
    zproc_daemonize (const char *workdir);

// Drop the process ID into the lockfile, with exclusive lock, and   
// switch the process to the specified group and/or user. Any of the 
// arguments may be null, indicating a no-op. Returns 0 on success,  
// -1 on failure. Note if you combine this with zsys_daemonize, run  
// after, not before that method, or the lockfile will hold the wrong
// process ID.                                                       
void
    zproc_run_as (const char *lockfile, const char *group, const char *user);

// Configure the number of I/O threads that ZeroMQ will use. A good  
// rule of thumb is one thread per gigabit of traffic in or out. The 
// default is 1, sufficient for most applications. If the environment
// variable ZSYS_IO_THREADS is defined, that provides the default.   
// Note that this method is valid only before any socket is created. 
void
    zproc_set_io_threads (size_t io_threads);

// Configure the number of sockets that ZeroMQ will allow. The default  
// is 1024. The actual limit depends on the system, and you can query it
// by using zsys_socket_limit (). A value of zero means "maximum".      
// Note that this method is valid only before any socket is created.    
void
    zproc_set_max_sockets (size_t max_sockets);

// Set network interface name to use for broadcasts, particularly zbeacon.    
// This lets the interface be configured for test environments where required.
// For example, on Mac OS X, zbeacon cannot bind to 255.255.255.255 which is  
// the default when there is no specified interface. If the environment       
// variable ZSYS_INTERFACE is set, use that as the default interface name.    
// Setting the interface to "*" means "use all available interfaces".         
void
    zproc_set_biface (const char *value);

// Return network interface to use for broadcasts, or "" if none was set.
const char *
    zproc_biface (void);

// Set log identity, which is a string that prefixes all log messages sent
// by this process. The log identity defaults to the environment variable 
// ZSYS_LOGIDENT, if that is set.                                         
void
    zproc_set_log_ident (const char *value);

// Sends log output to a PUB socket bound to the specified endpoint. To   
// collect such log output, create a SUB socket, subscribe to the traffic 
// you care about, and connect to the endpoint. Log traffic is sent as a  
// single string frame, in the same format as when sent to stdout. The    
// log system supports a single sender; multiple calls to this method will
// bind the same sender to multiple endpoints. To disable the sender, call
// this method with a null argument.                                      
void
    zproc_set_log_sender (const char *endpoint);

// Enable or disable logging to the system facility (syslog on POSIX boxes,
// event log on Windows). By default this is disabled.                     
void
    zproc_set_log_system (bool logsystem);

// Log error condition - highest priority
void
    zproc_log_error (const char *format, ...);

// Log warning condition - high priority
void
    zproc_log_warning (const char *format, ...);

// Log normal, but significant, condition - normal priority
void
    zproc_log_notice (const char *format, ...);

// Log informational message - low priority
void
    zproc_log_info (const char *format, ...);

// Log debug-level message - lowest priority
void
    zproc_log_debug (const char *format, ...);

// Self test of this class.
void
    zproc_test (bool verbose);

// CLASS: zsock
// Create a new socket. Returns the new socket, or NULL if the new socket
// could not be created. Note that the symbol zsock_new (and other       
// constructors/destructors for zsock) are redirected to the *_checked   
// variant, enabling intelligent socket leak detection. This can have    
// performance implications if you use a LOT of sockets. To turn off this
// redirection behaviour, define ZSOCK_NOCHECK.                          
zsock_t *
    zsock_new (int type);

// Destroy the socket. You must use this for any socket created via the
// zsock_new method.                                                   
void
    zsock_destroy (zsock_t **self_p);

// Create a PUB socket. Default action is bind.
zsock_t *
    zsock_new_pub (const char *endpoint);

// Create a SUB socket, and optionally subscribe to some prefix string. Default
// action is connect.                                                          
zsock_t *
    zsock_new_sub (const char *endpoint, const char *subscribe);

// Create a REQ socket. Default action is connect.
zsock_t *
    zsock_new_req (const char *endpoint);

// Create a REP socket. Default action is bind.
zsock_t *
    zsock_new_rep (const char *endpoint);

// Create a DEALER socket. Default action is connect.
zsock_t *
    zsock_new_dealer (const char *endpoint);

// Create a ROUTER socket. Default action is bind.
zsock_t *
    zsock_new_router (const char *endpoint);

// Create a PUSH socket. Default action is connect.
zsock_t *
    zsock_new_push (const char *endpoint);

// Create a PULL socket. Default action is bind.
zsock_t *
    zsock_new_pull (const char *endpoint);

// Create an XPUB socket. Default action is bind.
zsock_t *
    zsock_new_xpub (const char *endpoint);

// Create an XSUB socket. Default action is connect.
zsock_t *
    zsock_new_xsub (const char *endpoint);

// Create a PAIR socket. Default action is connect.
zsock_t *
    zsock_new_pair (const char *endpoint);

// Create a STREAM socket. Default action is connect.
zsock_t *
    zsock_new_stream (const char *endpoint);

// Create a SERVER socket. Default action is bind.
zsock_t *
    zsock_new_server (const char *endpoint);

// Create a CLIENT socket. Default action is connect.
zsock_t *
    zsock_new_client (const char *endpoint);

// Create a RADIO socket. Default action is bind.
zsock_t *
    zsock_new_radio (const char *endpoint);

// Create a DISH socket. Default action is connect.
zsock_t *
    zsock_new_dish (const char *endpoint);

// Create a GATHER socket. Default action is bind.
zsock_t *
    zsock_new_gather (const char *endpoint);

// Create a SCATTER socket. Default action is connect.
zsock_t *
    zsock_new_scatter (const char *endpoint);

// Bind a socket to a formatted endpoint. For tcp:// endpoints, supports   
// ephemeral ports, if you specify the port number as "*". By default      
// zsock uses the IANA designated range from C000 (49152) to FFFF (65535). 
// To override this range, follow the "*" with "[first-last]". Either or   
// both first and last may be empty. To bind to a random port within the   
// range, use "!" in place of "*".                                         
//                                                                         
// Examples:                                                               
//     tcp://127.0.0.1:*           bind to first free port from C000 up    
//     tcp://127.0.0.1:!           bind to random port from C000 to FFFF   
//     tcp://127.0.0.1:*[60000-]   bind to first free port from 60000 up   
//     tcp://127.0.0.1:![-60000]   bind to random port from C000 to 60000  
//     tcp://127.0.0.1:![55000-55999]                                      
//                                 bind to random port from 55000 to 55999 
//                                                                         
// On success, returns the actual port number used, for tcp:// endpoints,  
// and 0 for other transports. On failure, returns -1. Note that when using
// ephemeral ports, a port may be reused by different services without     
// clients being aware. Protocols that run on ephemeral ports should take  
// this into account.                                                      
int
    zsock_bind (zsock_t *self, const char *format, ...);

// Returns last bound endpoint, if any.
const char *
    zsock_endpoint (zsock_t *self);

// Unbind a socket from a formatted endpoint.                     
// Returns 0 if OK, -1 if the endpoint was invalid or the function
// isn't supported.                                               
int
    zsock_unbind (zsock_t *self, const char *format, ...);

// Connect a socket to a formatted endpoint        
// Returns 0 if OK, -1 if the endpoint was invalid.
int
    zsock_connect (zsock_t *self, const char *format, ...);

// Disconnect a socket from a formatted endpoint                  
// Returns 0 if OK, -1 if the endpoint was invalid or the function
// isn't supported.                                               
int
    zsock_disconnect (zsock_t *self, const char *format, ...);

// Attach a socket to zero or more endpoints. If endpoints is not null,     
// parses as list of ZeroMQ endpoints, separated by commas, and prefixed by 
// '@' (to bind the socket) or '>' (to connect the socket). Returns 0 if all
// endpoints were valid, or -1 if there was a syntax error. If the endpoint 
// does not start with '@' or '>', the serverish argument defines whether   
// it is used to bind (serverish = true) or connect (serverish = false).    
int
    zsock_attach (zsock_t *self, const char *endpoints, bool serverish);

// Returns socket type as printable constant string.
const char *
    zsock_type_str (zsock_t *self);

// Send a 'picture' message to the socket (or actor). The picture is a   
// string that defines the type of each frame. This makes it easy to send
// a complex multiframe message in one call. The picture can contain any 
// of these characters, each corresponding to one or two arguments:      
//                                                                       
//     i = int (signed)                                                  
//     1 = uint8_t                                                       
//     2 = uint16_t                                                      
//     4 = uint32_t                                                      
//     8 = uint64_t                                                      
//     s = char *                                                        
//     b = byte *, size_t (2 arguments)                                  
//     c = zchunk_t *                                                    
//     f = zframe_t *                                                    
//     h = zhashx_t *                                                    
//     U = zuuid_t *                                                     
//     p = void * (sends the pointer value, only meaningful over inproc) 
//     m = zmsg_t * (sends all frames in the zmsg)                       
//     z = sends zero-sized frame (0 arguments)                          
//     u = uint (deprecated)                                             
//                                                                       
// Note that s, b, c, and f are encoded the same way and the choice is   
// offered as a convenience to the sender, which may or may not already  
// have data in a zchunk or zframe. Does not change or take ownership of 
// any arguments. Returns 0 if successful, -1 if sending failed for any  
// reason.                                                               
int
    zsock_send (void *self, const char *picture, ...);

// Send a 'picture' message to the socket (or actor). This is a va_list 
// version of zsock_send (), so please consult its documentation for the
// details.                                                             
int
    zsock_vsend (void *self, const char *picture, va_list argptr);

// Receive a 'picture' message to the socket (or actor). See zsock_send for
// the format and meaning of the picture. Returns the picture elements into
// a series of pointers as provided by the caller:                         
//                                                                         
//     i = int * (stores signed integer)                                   
//     4 = uint32_t * (stores 32-bit unsigned integer)                     
//     8 = uint64_t * (stores 64-bit unsigned integer)                     
//     s = char ** (allocates new string)                                  
//     b = byte **, size_t * (2 arguments) (allocates memory)              
//     c = zchunk_t ** (creates zchunk)                                    
//     f = zframe_t ** (creates zframe)                                    
//     U = zuuid_t * (creates a zuuid with the data)                       
//     h = zhashx_t ** (creates zhashx)                                    
//     p = void ** (stores pointer)                                        
//     m = zmsg_t ** (creates a zmsg with the remaing frames)              
//     z = null, asserts empty frame (0 arguments)                         
//     u = uint * (stores unsigned integer, deprecated)                    
//                                                                         
// Note that zsock_recv creates the returned objects, and the caller must  
// destroy them when finished with them. The supplied pointers do not need 
// to be initialized. Returns 0 if successful, or -1 if it failed to recv  
// a message, in which case the pointers are not modified. When message    
// frames are truncated (a short message), sets return values to zero/null.
// If an argument pointer is NULL, does not store any value (skips it).    
// An 'n' picture matches an empty frame; if the message does not match,   
// the method will return -1.                                              
int
    zsock_recv (void *self, const char *picture, ...);

// Receive a 'picture' message from the socket (or actor). This is a    
// va_list version of zsock_recv (), so please consult its documentation
// for the details.                                                     
int
    zsock_vrecv (void *self, const char *picture, va_list argptr);

// Send a binary encoded 'picture' message to the socket (or actor). This 
// method is similar to zsock_send, except the arguments are encoded in a 
// binary format that is compatible with zproto, and is designed to reduce
// memory allocations. The pattern argument is a string that defines the  
// type of each argument. Supports these argument types:                  
//                                                                        
//  pattern    C type                  zproto type:                       
//     1       uint8_t                 type = "number" size = "1"         
//     2       uint16_t                type = "number" size = "2"         
//     4       uint32_t                type = "number" size = "3"         
//     8       uint64_t                type = "number" size = "4"         
//     s       char *, 0-255 chars     type = "string"                    
//     S       char *, 0-2^32-1 chars  type = "longstr"                   
//     c       zchunk_t *              type = "chunk"                     
//     f       zframe_t *              type = "frame"                     
//     u       zuuid_t *               type = "uuid"                      
//     m       zmsg_t *                type = "msg"                       
//     p       void *, sends pointer value, only over inproc              
//                                                                        
// Does not change or take ownership of any arguments. Returns 0 if       
// successful, -1 if sending failed for any reason.                       
int
    zsock_bsend (void *self, const char *picture, ...);

// Receive a binary encoded 'picture' message from the socket (or actor).  
// This method is similar to zsock_recv, except the arguments are encoded  
// in a binary format that is compatible with zproto, and is designed to   
// reduce memory allocations. The pattern argument is a string that defines
// the type of each argument. See zsock_bsend for the supported argument   
// types. All arguments must be pointers; this call sets them to point to  
// values held on a per-socket basis.                                      
// Note that zsock_brecv creates the returned objects, and the caller must 
// destroy them when finished with them. The supplied pointers do not need 
// to be initialized. Returns 0 if successful, or -1 if it failed to read  
// a message.                                                              
int
    zsock_brecv (void *self, const char *picture, ...);

// Return socket routing ID if any. This returns 0 if the socket is not
// of type ZMQ_SERVER or if no request was already received on it.     
uint32_t
    zsock_routing_id (zsock_t *self);

// Set routing ID on socket. The socket MUST be of type ZMQ_SERVER.        
// This will be used when sending messages on the socket via the zsock API.
void
    zsock_set_routing_id (zsock_t *self, uint32_t routing_id);

// Set socket to use unbounded pipes (HWM=0); use this in cases when you are
// totally certain the message volume can fit in memory. This method works  
// across all versions of ZeroMQ. Takes a polymorphic socket reference.     
void
    zsock_set_unbounded (void *self);

// Send a signal over a socket. A signal is a short message carrying a   
// success/failure code (by convention, 0 means OK). Signals are encoded 
// to be distinguishable from "normal" messages. Accepts a zsock_t or a  
// zactor_t argument, and returns 0 if successful, -1 if the signal could
// not be sent. Takes a polymorphic socket reference.                    
int
    zsock_signal (void *self, byte status);

// Wait on a signal. Use this to coordinate between threads, over pipe  
// pairs. Blocks until the signal is received. Returns -1 on error, 0 or
// greater on success. Accepts a zsock_t or a zactor_t as argument.     
// Takes a polymorphic socket reference.                                
int
    zsock_wait (void *self);

// If there is a partial message still waiting on the socket, remove and    
// discard it. This is useful when reading partial messages, to get specific
// message types.                                                           
void
    zsock_flush (void *self);

// Join a group for the RADIO-DISH pattern. Call only on ZMQ_DISH.
// Returns 0 if OK, -1 if failed.                                 
int
    zsock_join (void *self, const char *group);

// Leave a group for the RADIO-DISH pattern. Call only on ZMQ_DISH.
// Returns 0 if OK, -1 if failed.                                  
int
    zsock_leave (void *self, const char *group);

// Probe the supplied object, and report if it looks like a zsock_t.
// Takes a polymorphic socket reference.                            
bool
    zsock_is (void *self);

// Probe the supplied reference. If it looks like a zsock_t instance, return
// the underlying libzmq socket handle; else if it looks like a file        
// descriptor, return NULL; else if it looks like a libzmq socket handle,   
// return the supplied value. Takes a polymorphic socket reference.         
void *
    zsock_resolve (void *self);

// Get socket option `heartbeat_ivl`.
// Available from libzmq 4.2.0.      
int
    zsock_heartbeat_ivl (void *self);

// Set socket option `heartbeat_ivl`.
// Available from libzmq 4.2.0.      
void
    zsock_set_heartbeat_ivl (void *self, int heartbeat_ivl);

// Get socket option `heartbeat_ttl`.
// Available from libzmq 4.2.0.      
int
    zsock_heartbeat_ttl (void *self);

// Set socket option `heartbeat_ttl`.
// Available from libzmq 4.2.0.      
void
    zsock_set_heartbeat_ttl (void *self, int heartbeat_ttl);

// Get socket option `heartbeat_timeout`.
// Available from libzmq 4.2.0.          
int
    zsock_heartbeat_timeout (void *self);

// Set socket option `heartbeat_timeout`.
// Available from libzmq 4.2.0.          
void
    zsock_set_heartbeat_timeout (void *self, int heartbeat_timeout);

// Get socket option `use_fd`. 
// Available from libzmq 4.2.0.
int
    zsock_use_fd (void *self);

// Set socket option `use_fd`. 
// Available from libzmq 4.2.0.
void
    zsock_set_use_fd (void *self, int use_fd);

// Set socket option `xpub_manual`.
// Available from libzmq 4.2.0.    
void
    zsock_set_xpub_manual (void *self, int xpub_manual);

// Set socket option `xpub_welcome_msg`.
// Available from libzmq 4.2.0.         
void
    zsock_set_xpub_welcome_msg (void *self, const char *xpub_welcome_msg);

// Set socket option `stream_notify`.
// Available from libzmq 4.2.0.      
void
    zsock_set_stream_notify (void *self, int stream_notify);

// Get socket option `invert_matching`.
// Available from libzmq 4.2.0.        
int
    zsock_invert_matching (void *self);

// Set socket option `invert_matching`.
// Available from libzmq 4.2.0.        
void
    zsock_set_invert_matching (void *self, int invert_matching);

// Set socket option `xpub_verboser`.
// Available from libzmq 4.2.0.      
void
    zsock_set_xpub_verboser (void *self, int xpub_verboser);

// Get socket option `connect_timeout`.
// Available from libzmq 4.2.0.        
int
    zsock_connect_timeout (void *self);

// Set socket option `connect_timeout`.
// Available from libzmq 4.2.0.        
void
    zsock_set_connect_timeout (void *self, int connect_timeout);

// Get socket option `tcp_maxrt`.
// Available from libzmq 4.2.0.  
int
    zsock_tcp_maxrt (void *self);

// Set socket option `tcp_maxrt`.
// Available from libzmq 4.2.0.  
void
    zsock_set_tcp_maxrt (void *self, int tcp_maxrt);

// Get socket option `thread_safe`.
// Available from libzmq 4.2.0.    
int
    zsock_thread_safe (void *self);

// Get socket option `multicast_maxtpdu`.
// Available from libzmq 4.2.0.          
int
    zsock_multicast_maxtpdu (void *self);

// Set socket option `multicast_maxtpdu`.
// Available from libzmq 4.2.0.          
void
    zsock_set_multicast_maxtpdu (void *self, int multicast_maxtpdu);

// Get socket option `vmci_buffer_size`.
// Available from libzmq 4.2.0.         
int
    zsock_vmci_buffer_size (void *self);

// Set socket option `vmci_buffer_size`.
// Available from libzmq 4.2.0.         
void
    zsock_set_vmci_buffer_size (void *self, int vmci_buffer_size);

// Get socket option `vmci_buffer_min_size`.
// Available from libzmq 4.2.0.             
int
    zsock_vmci_buffer_min_size (void *self);

// Set socket option `vmci_buffer_min_size`.
// Available from libzmq 4.2.0.             
void
    zsock_set_vmci_buffer_min_size (void *self, int vmci_buffer_min_size);

// Get socket option `vmci_buffer_max_size`.
// Available from libzmq 4.2.0.             
int
    zsock_vmci_buffer_max_size (void *self);

// Set socket option `vmci_buffer_max_size`.
// Available from libzmq 4.2.0.             
void
    zsock_set_vmci_buffer_max_size (void *self, int vmci_buffer_max_size);

// Get socket option `vmci_connect_timeout`.
// Available from libzmq 4.2.0.             
int
    zsock_vmci_connect_timeout (void *self);

// Set socket option `vmci_connect_timeout`.
// Available from libzmq 4.2.0.             
void
    zsock_set_vmci_connect_timeout (void *self, int vmci_connect_timeout);

// Get socket option `tos`.    
// Available from libzmq 4.1.0.
int
    zsock_tos (void *self);

// Set socket option `tos`.    
// Available from libzmq 4.1.0.
void
    zsock_set_tos (void *self, int tos);

// Set socket option `router_handover`.
// Available from libzmq 4.1.0.        
void
    zsock_set_router_handover (void *self, int router_handover);

// Set socket option `connect_rid`.
// Available from libzmq 4.1.0.    
void
    zsock_set_connect_rid (void *self, const char *connect_rid);

// Set socket option `connect_rid` from 32-octet binary
// Available from libzmq 4.1.0.                        
void
    zsock_set_connect_rid_bin (void *self, const byte *connect_rid);

// Get socket option `handshake_ivl`.
// Available from libzmq 4.1.0.      
int
    zsock_handshake_ivl (void *self);

// Set socket option `handshake_ivl`.
// Available from libzmq 4.1.0.      
void
    zsock_set_handshake_ivl (void *self, int handshake_ivl);

// Get socket option `socks_proxy`.
// Available from libzmq 4.1.0.    
char *
    zsock_socks_proxy (void *self);

// Set socket option `socks_proxy`.
// Available from libzmq 4.1.0.    
void
    zsock_set_socks_proxy (void *self, const char *socks_proxy);

// Set socket option `xpub_nodrop`.
// Available from libzmq 4.1.0.    
void
    zsock_set_xpub_nodrop (void *self, int xpub_nodrop);

// Set socket option `router_mandatory`.
// Available from libzmq 4.0.0.         
void
    zsock_set_router_mandatory (void *self, int router_mandatory);

// Set socket option `probe_router`.
// Available from libzmq 4.0.0.     
void
    zsock_set_probe_router (void *self, int probe_router);

// Set socket option `req_relaxed`.
// Available from libzmq 4.0.0.    
void
    zsock_set_req_relaxed (void *self, int req_relaxed);

// Set socket option `req_correlate`.
// Available from libzmq 4.0.0.      
void
    zsock_set_req_correlate (void *self, int req_correlate);

// Set socket option `conflate`.
// Available from libzmq 4.0.0. 
void
    zsock_set_conflate (void *self, int conflate);

// Get socket option `zap_domain`.
// Available from libzmq 4.0.0.   
char *
    zsock_zap_domain (void *self);

// Set socket option `zap_domain`.
// Available from libzmq 4.0.0.   
void
    zsock_set_zap_domain (void *self, const char *zap_domain);

// Get socket option `mechanism`.
// Available from libzmq 4.0.0.  
int
    zsock_mechanism (void *self);

// Get socket option `plain_server`.
// Available from libzmq 4.0.0.     
int
    zsock_plain_server (void *self);

// Set socket option `plain_server`.
// Available from libzmq 4.0.0.     
void
    zsock_set_plain_server (void *self, int plain_server);

// Get socket option `plain_username`.
// Available from libzmq 4.0.0.       
char *
    zsock_plain_username (void *self);

// Set socket option `plain_username`.
// Available from libzmq 4.0.0.       
void
    zsock_set_plain_username (void *self, const char *plain_username);

// Get socket option `plain_password`.
// Available from libzmq 4.0.0.       
char *
    zsock_plain_password (void *self);

// Set socket option `plain_password`.
// Available from libzmq 4.0.0.       
void
    zsock_set_plain_password (void *self, const char *plain_password);

// Get socket option `curve_server`.
// Available from libzmq 4.0.0.     
int
    zsock_curve_server (void *self);

// Set socket option `curve_server`.
// Available from libzmq 4.0.0.     
void
    zsock_set_curve_server (void *self, int curve_server);

// Get socket option `curve_publickey`.
// Available from libzmq 4.0.0.        
char *
    zsock_curve_publickey (void *self);

// Set socket option `curve_publickey`.
// Available from libzmq 4.0.0.        
void
    zsock_set_curve_publickey (void *self, const char *curve_publickey);

// Set socket option `curve_publickey` from 32-octet binary
// Available from libzmq 4.0.0.                            
void
    zsock_set_curve_publickey_bin (void *self, const byte *curve_publickey);

// Get socket option `curve_secretkey`.
// Available from libzmq 4.0.0.        
char *
    zsock_curve_secretkey (void *self);

// Set socket option `curve_secretkey`.
// Available from libzmq 4.0.0.        
void
    zsock_set_curve_secretkey (void *self, const char *curve_secretkey);

// Set socket option `curve_secretkey` from 32-octet binary
// Available from libzmq 4.0.0.                            
void
    zsock_set_curve_secretkey_bin (void *self, const byte *curve_secretkey);

// Get socket option `curve_serverkey`.
// Available from libzmq 4.0.0.        
char *
    zsock_curve_serverkey (void *self);

// Set socket option `curve_serverkey`.
// Available from libzmq 4.0.0.        
void
    zsock_set_curve_serverkey (void *self, const char *curve_serverkey);

// Set socket option `curve_serverkey` from 32-octet binary
// Available from libzmq 4.0.0.                            
void
    zsock_set_curve_serverkey_bin (void *self, const byte *curve_serverkey);

// Get socket option `gssapi_server`.
// Available from libzmq 4.0.0.      
int
    zsock_gssapi_server (void *self);

// Set socket option `gssapi_server`.
// Available from libzmq 4.0.0.      
void
    zsock_set_gssapi_server (void *self, int gssapi_server);

// Get socket option `gssapi_plaintext`.
// Available from libzmq 4.0.0.         
int
    zsock_gssapi_plaintext (void *self);

// Set socket option `gssapi_plaintext`.
// Available from libzmq 4.0.0.         
void
    zsock_set_gssapi_plaintext (void *self, int gssapi_plaintext);

// Get socket option `gssapi_principal`.
// Available from libzmq 4.0.0.         
char *
    zsock_gssapi_principal (void *self);

// Set socket option `gssapi_principal`.
// Available from libzmq 4.0.0.         
void
    zsock_set_gssapi_principal (void *self, const char *gssapi_principal);

// Get socket option `gssapi_service_principal`.
// Available from libzmq 4.0.0.                 
char *
    zsock_gssapi_service_principal (void *self);

// Set socket option `gssapi_service_principal`.
// Available from libzmq 4.0.0.                 
void
    zsock_set_gssapi_service_principal (void *self, const char *gssapi_service_principal);

// Get socket option `ipv6`.   
// Available from libzmq 4.0.0.
int
    zsock_ipv6 (void *self);

// Set socket option `ipv6`.   
// Available from libzmq 4.0.0.
void
    zsock_set_ipv6 (void *self, int ipv6);

// Get socket option `immediate`.
// Available from libzmq 4.0.0.  
int
    zsock_immediate (void *self);

// Set socket option `immediate`.
// Available from libzmq 4.0.0.  
void
    zsock_set_immediate (void *self, int immediate);

// Get socket option `sndhwm`. 
// Available from libzmq 3.0.0.
int
    zsock_sndhwm (void *self);

// Set socket option `sndhwm`. 
// Available from libzmq 3.0.0.
void
    zsock_set_sndhwm (void *self, int sndhwm);

// Get socket option `rcvhwm`. 
// Available from libzmq 3.0.0.
int
    zsock_rcvhwm (void *self);

// Set socket option `rcvhwm`. 
// Available from libzmq 3.0.0.
void
    zsock_set_rcvhwm (void *self, int rcvhwm);

// Get socket option `maxmsgsize`.
// Available from libzmq 3.0.0.   
int
    zsock_maxmsgsize (void *self);

// Set socket option `maxmsgsize`.
// Available from libzmq 3.0.0.   
void
    zsock_set_maxmsgsize (void *self, int maxmsgsize);

// Get socket option `multicast_hops`.
// Available from libzmq 3.0.0.       
int
    zsock_multicast_hops (void *self);

// Set socket option `multicast_hops`.
// Available from libzmq 3.0.0.       
void
    zsock_set_multicast_hops (void *self, int multicast_hops);

// Set socket option `xpub_verbose`.
// Available from libzmq 3.0.0.     
void
    zsock_set_xpub_verbose (void *self, int xpub_verbose);

// Get socket option `tcp_keepalive`.
// Available from libzmq 3.0.0.      
int
    zsock_tcp_keepalive (void *self);

// Set socket option `tcp_keepalive`.
// Available from libzmq 3.0.0.      
void
    zsock_set_tcp_keepalive (void *self, int tcp_keepalive);

// Get socket option `tcp_keepalive_idle`.
// Available from libzmq 3.0.0.           
int
    zsock_tcp_keepalive_idle (void *self);

// Set socket option `tcp_keepalive_idle`.
// Available from libzmq 3.0.0.           
void
    zsock_set_tcp_keepalive_idle (void *self, int tcp_keepalive_idle);

// Get socket option `tcp_keepalive_cnt`.
// Available from libzmq 3.0.0.          
int
    zsock_tcp_keepalive_cnt (void *self);

// Set socket option `tcp_keepalive_cnt`.
// Available from libzmq 3.0.0.          
void
    zsock_set_tcp_keepalive_cnt (void *self, int tcp_keepalive_cnt);

// Get socket option `tcp_keepalive_intvl`.
// Available from libzmq 3.0.0.            
int
    zsock_tcp_keepalive_intvl (void *self);

// Set socket option `tcp_keepalive_intvl`.
// Available from libzmq 3.0.0.            
void
    zsock_set_tcp_keepalive_intvl (void *self, int tcp_keepalive_intvl);

// Get socket option `tcp_accept_filter`.
// Available from libzmq 3.0.0.          
char *
    zsock_tcp_accept_filter (void *self);

// Set socket option `tcp_accept_filter`.
// Available from libzmq 3.0.0.          
void
    zsock_set_tcp_accept_filter (void *self, const char *tcp_accept_filter);

// Get socket option `last_endpoint`.
// Available from libzmq 3.0.0.      
char *
    zsock_last_endpoint (void *self);

// Set socket option `router_raw`.
// Available from libzmq 3.0.0.   
void
    zsock_set_router_raw (void *self, int router_raw);

// Get socket option `ipv4only`.
// Available from libzmq 3.0.0. 
int
    zsock_ipv4only (void *self);

// Set socket option `ipv4only`.
// Available from libzmq 3.0.0. 
void
    zsock_set_ipv4only (void *self, int ipv4only);

// Set socket option `delay_attach_on_connect`.
// Available from libzmq 3.0.0.                
void
    zsock_set_delay_attach_on_connect (void *self, int delay_attach_on_connect);

// Get socket option `hwm`.             
// Available from libzmq 2.0.0 to 3.0.0.
int
    zsock_hwm (void *self);

// Set socket option `hwm`.             
// Available from libzmq 2.0.0 to 3.0.0.
void
    zsock_set_hwm (void *self, int hwm);

// Get socket option `swap`.            
// Available from libzmq 2.0.0 to 3.0.0.
int
    zsock_swap (void *self);

// Set socket option `swap`.            
// Available from libzmq 2.0.0 to 3.0.0.
void
    zsock_set_swap (void *self, int swap);

// Get socket option `affinity`.
// Available from libzmq 2.0.0. 
int
    zsock_affinity (void *self);

// Set socket option `affinity`.
// Available from libzmq 2.0.0. 
void
    zsock_set_affinity (void *self, int affinity);

// Get socket option `identity`.
// Available from libzmq 2.0.0. 
char *
    zsock_identity (void *self);

// Set socket option `identity`.
// Available from libzmq 2.0.0. 
void
    zsock_set_identity (void *self, const char *identity);

// Get socket option `rate`.   
// Available from libzmq 2.0.0.
int
    zsock_rate (void *self);

// Set socket option `rate`.   
// Available from libzmq 2.0.0.
void
    zsock_set_rate (void *self, int rate);

// Get socket option `recovery_ivl`.
// Available from libzmq 2.0.0.     
int
    zsock_recovery_ivl (void *self);

// Set socket option `recovery_ivl`.
// Available from libzmq 2.0.0.     
void
    zsock_set_recovery_ivl (void *self, int recovery_ivl);

// Get socket option `recovery_ivl_msec`.
// Available from libzmq 2.0.0 to 3.0.0. 
int
    zsock_recovery_ivl_msec (void *self);

// Set socket option `recovery_ivl_msec`.
// Available from libzmq 2.0.0 to 3.0.0. 
void
    zsock_set_recovery_ivl_msec (void *self, int recovery_ivl_msec);

// Get socket option `mcast_loop`.      
// Available from libzmq 2.0.0 to 3.0.0.
int
    zsock_mcast_loop (void *self);

// Set socket option `mcast_loop`.      
// Available from libzmq 2.0.0 to 3.0.0.
void
    zsock_set_mcast_loop (void *self, int mcast_loop);

// Get socket option `rcvtimeo`.
// Available from libzmq 2.2.0. 
int
    zsock_rcvtimeo (void *self);

// Set socket option `rcvtimeo`.
// Available from libzmq 2.2.0. 
void
    zsock_set_rcvtimeo (void *self, int rcvtimeo);

// Get socket option `sndtimeo`.
// Available from libzmq 2.2.0. 
int
    zsock_sndtimeo (void *self);

// Set socket option `sndtimeo`.
// Available from libzmq 2.2.0. 
void
    zsock_set_sndtimeo (void *self, int sndtimeo);

// Get socket option `sndbuf`. 
// Available from libzmq 2.0.0.
int
    zsock_sndbuf (void *self);

// Set socket option `sndbuf`. 
// Available from libzmq 2.0.0.
void
    zsock_set_sndbuf (void *self, int sndbuf);

// Get socket option `rcvbuf`. 
// Available from libzmq 2.0.0.
int
    zsock_rcvbuf (void *self);

// Set socket option `rcvbuf`. 
// Available from libzmq 2.0.0.
void
    zsock_set_rcvbuf (void *self, int rcvbuf);

// Get socket option `linger`. 
// Available from libzmq 2.0.0.
int
    zsock_linger (void *self);

// Set socket option `linger`. 
// Available from libzmq 2.0.0.
void
    zsock_set_linger (void *self, int linger);

// Get socket option `reconnect_ivl`.
// Available from libzmq 2.0.0.      
int
    zsock_reconnect_ivl (void *self);

// Set socket option `reconnect_ivl`.
// Available from libzmq 2.0.0.      
void
    zsock_set_reconnect_ivl (void *self, int reconnect_ivl);

// Get socket option `reconnect_ivl_max`.
// Available from libzmq 2.0.0.          
int
    zsock_reconnect_ivl_max (void *self);

// Set socket option `reconnect_ivl_max`.
// Available from libzmq 2.0.0.          
void
    zsock_set_reconnect_ivl_max (void *self, int reconnect_ivl_max);

// Get socket option `backlog`.
// Available from libzmq 2.0.0.
int
    zsock_backlog (void *self);

// Set socket option `backlog`.
// Available from libzmq 2.0.0.
void
    zsock_set_backlog (void *self, int backlog);

// Set socket option `subscribe`.
// Available from libzmq 2.0.0.  
void
    zsock_set_subscribe (void *self, const char *subscribe);

// Set socket option `unsubscribe`.
// Available from libzmq 2.0.0.    
void
    zsock_set_unsubscribe (void *self, const char *unsubscribe);

// Get socket option `type`.   
// Available from libzmq 2.0.0.
int
    zsock_type (void *self);

// Get socket option `rcvmore`.
// Available from libzmq 2.0.0.
int
    zsock_rcvmore (void *self);

// Get socket option `fd`.     
// Available from libzmq 2.0.0.
SOCKET
    zsock_fd (void *self);

// Get socket option `events`. 
// Available from libzmq 2.0.0.
int
    zsock_events (void *self);

// Self test of this class.
void
    zsock_test (bool verbose);

// CLASS: zstr
// Receive C string from socket. Caller must free returned string using
// zstr_free(). Returns NULL if the context is being terminated or the 
// process was interrupted.                                            
char *
    zstr_recv (void *source);

// Receive a series of strings (until NULL) from multipart data.    
// Each string is allocated and filled with string data; if there   
// are not enough frames, unallocated strings are set to NULL.      
// Returns -1 if the message could not be read, else returns the    
// number of strings filled, zero or more. Free each returned string
// using zstr_free(). If not enough strings are provided, remaining 
// multipart frames in the message are dropped.                     
int
    zstr_recvx (void *source, char **string_p, ...);

// Send a C string to a socket, as a frame. The string is sent without 
// trailing null byte; to read this you can use zstr_recv, or a similar
// method that adds a null terminator on the received string. String   
// may be NULL, which is sent as "".                                   
int
    zstr_send (void *dest, const char *string);

// Send a C string to a socket, as zstr_send(), with a MORE flag, so that
// you can send further strings in the same multi-part message.          
int
    zstr_sendm (void *dest, const char *string);

// Send a formatted string to a socket. Note that you should NOT use
// user-supplied strings in the format (they may contain '%' which  
// will create security holes).                                     
int
    zstr_sendf (void *dest, const char *format, ...);

// Send a formatted string to a socket, as for zstr_sendf(), with a      
// MORE flag, so that you can send further strings in the same multi-part
// message.                                                              
int
    zstr_sendfm (void *dest, const char *format, ...);

// Send a series of strings (until NULL) as multipart data   
// Returns 0 if the strings could be sent OK, or -1 on error.
int
    zstr_sendx (void *dest, const char *string, ...);

// Accepts a void pointer and returns a fresh character string. If source
// is null, returns an empty string.                                     
char *
    zstr_str (void *source);

// Free a provided string, and nullify the parent pointer. Safe to call on
// a null pointer.                                                        
void
    zstr_free (char **string_p);

// Self test of this class.
void
    zstr_test (bool verbose);

// CLASS: ztimerset
// Create new timer set.
ztimerset_t *
    ztimerset_new (void);

// Destroy a timer set
void
    ztimerset_destroy (ztimerset_t **self_p);

// Add a timer to the set. Returns timer id if OK, -1 on failure.
int
    ztimerset_add (ztimerset_t *self, size_t interval, ztimerset_fn handler, void *arg);

// Cancel a timer. Returns 0 if OK, -1 on failure.
int
    ztimerset_cancel (ztimerset_t *self, int timer_id);

// Set timer interval. Returns 0 if OK, -1 on failure.                                    
// This method is slow, canceling the timer and adding a new one yield better performance.
int
    ztimerset_set_interval (ztimerset_t *self, int timer_id, size_t interval);

// Reset timer to start interval counting from current time. Returns 0 if OK, -1 on failure.
// This method is slow, canceling the timer and adding a new one yield better performance.  
int
    ztimerset_reset (ztimerset_t *self, int timer_id);

// Return the time until the next interval.                        
// Should be used as timeout parameter for the zpoller wait method.
// The timeout is in msec.                                         
int
    ztimerset_timeout (ztimerset_t *self);

// Invoke callback function of all timers which their interval has elapsed.
// Should be call after zpoller wait method.                               
// Returns 0 if OK, -1 on failure.                                         
int
    ztimerset_execute (ztimerset_t *self);

// Self test of this class.
void
    ztimerset_test (bool verbose);

// CLASS: ztrie
// Creates a new ztrie.
ztrie_t *
    ztrie_new (char delimiter);

// Destroy the ztrie.
void
    ztrie_destroy (ztrie_t **self_p);

// Inserts a new route into the tree and attaches the data. Returns -1     
// if the route already exists, otherwise 0. This method takes ownership of
// the provided data if a destroy_data_fn is provided.                     
int
    ztrie_insert_route (ztrie_t *self, const char *path, void *data, ztrie_destroy_data_fn destroy_data_fn);

// Removes a route from the trie and destroys its data. Returns -1 if the
// route does not exists, otherwise 0.                                   
// the start of the list call zlist_first (). Advances the cursor.       
int
    ztrie_remove_route (ztrie_t *self, const char *path);

// Returns true if the path matches a route in the tree, otherwise false.
bool
    ztrie_matches (ztrie_t *self, const char *path);

// Returns the data of a matched route from last ztrie_matches. If the path
// did not match, returns NULL. Do not delete the data as it's owned by    
// ztrie.                                                                  
void *
    ztrie_hit_data (ztrie_t *self);

// Returns the count of parameters that a matched route has.
size_t
    ztrie_hit_parameter_count (ztrie_t *self);

// Returns the parameters of a matched route with named regexes from last   
// ztrie_matches. If the path did not match or the route did not contain any
// named regexes, returns NULL.                                             
zhashx_t *
    ztrie_hit_parameters (ztrie_t *self);

// Returns the asterisk matched part of a route, if there has been no match
// or no asterisk match, returns NULL.                                     
const char *
    ztrie_hit_asterisk_match (ztrie_t *self);

// Print the trie
void
    ztrie_print (ztrie_t *self);

// Self test of this class.
void
    ztrie_test (bool verbose);

// CLASS: zuuid
// Create a new UUID object.
zuuid_t *
    zuuid_new (void);

// Destroy a specified UUID object.
void
    zuuid_destroy (zuuid_t **self_p);

// Create UUID object from supplied ZUUID_LEN-octet value.
zuuid_t *
    zuuid_new_from (const byte *source);

// Set UUID to new supplied ZUUID_LEN-octet value.
void
    zuuid_set (zuuid_t *self, const byte *source);

// Set UUID to new supplied string value skipping '-' and '{' '}'
// optional delimiters. Return 0 if OK, else returns -1.         
int
    zuuid_set_str (zuuid_t *self, const char *source);

// Return UUID binary data.
const byte *
    zuuid_data (zuuid_t *self);

// Return UUID binary size
size_t
    zuuid_size (zuuid_t *self);

// Returns UUID as string
const char *
    zuuid_str (zuuid_t *self);

// Return UUID in the canonical string format: 8-4-4-4-12, in lower
// case. Caller does not modify or free returned value. See        
// http://en.wikipedia.org/wiki/Universally_unique_identifier      
const char *
    zuuid_str_canonical (zuuid_t *self);

// Store UUID blob in target array
void
    zuuid_export (zuuid_t *self, byte *target);

// Check if UUID is same as supplied value
bool
    zuuid_eq (zuuid_t *self, const byte *compare);

// Check if UUID is different from supplied value
bool
    zuuid_neq (zuuid_t *self, const byte *compare);

// Make copy of UUID object; if uuid is null, or memory was exhausted,
// returns null.                                                      
zuuid_t *
    zuuid_dup (zuuid_t *self);

// Self test of this class.
void
    zuuid_test (bool verbose);

''')
for i, item in enumerate (czmq_cdefs):
    czmq_cdefs [i] = re.sub(r';[^;]*\bva_list\b[^;]*;', ';', item, flags=re.S) # we don't support anything with a va_list arg

