# shortfoot

## Script interface

* Each script takes a headerless TSV file.
* For each row:
  * The script selects one or more columns as input, with the column indices
    specified in command line arguments.
  * The script can choose to discard the row.
  * The script appends the output as additional columns.

## Other conversions

### English to ASCII Braille

To correctly translate into Contracted (Grade 2) Braille:

* Install `liblouisutdml-bin`
* Prepare a file where each word is in its own line, **separated by a blank line**.
  * The command `sed G infile` can add a blank line between consecutive lines.
* Run`
  ```
  file2brl infile outfile
  ```

