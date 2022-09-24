# seq_to_spindle_dirart
Convert .seq file from Marq's PETSCII editor to spindle 2.3 compatible directory art

```
usage: seq_to_spindle_dirart.py filename.seq [linelen=16]
```

## Example workflow

### Create the dir art

1. Create directory art with [Marq's PETSCII editor](http://www.kameli.net/marq/?page_id=2717). Use 'Dir Art' mode for editing.
2. Once ready, exit the editor and load the image in C64 mode, as sequential file export does not work in Dir Art mode. 
3. Export the picture as `.seq` (press <kbd>q</kbd>).

### Convert the dir art

```sh
python seq_to_spindle_dirart.py dirart.seq > dirart.txt
```

### Import the dir art to Spindle

```sh
spin.exe -vv -a dirart.txt -o disk.d64 script
```
