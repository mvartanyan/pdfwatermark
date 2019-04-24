# Why?
I needed to "stamp" quite a bunch of PDF files with a large transparent text mark.
The mark content depended on the PDF file name. 
I looked around and realised that I can't seem to be able to find anything that
would help me get it done in Linux without major pain of some sort. So I decided 
to roll my own

# What it does. 
`pdfwatermark` allows you to add an arbitrary text line on the first page of
a given PDF file. You can also make the text of the watermark depend on the file
name. 

# Usage

`$ python pdfwatermark.py [OPTIONS] FILENAME`

Use `--help` to see the detailed list of options

## Warning
By default, `pdfwatermark` watermarks the file in place. No way to 
'unwatermark' it is provided.

## Example

**Example 1, "trivial"**

`python pdfwatermark.py -w "WATERMARK" file.pdf`

Puts a large black text 'WATERMARK' somewhere on the first page of `file.pdf`

**Example 2, "simple"**

`python pdfwatermark.py -w "WATERMARK" -c "#FF0000" -o 0.3 -x 200 -y 150  file.pdf` 

Puts a large transparent pink 'WATERMARK' at the given coordinates 
on the first page of `file.pdf`


**Example 2, "pdfwatermark in full glory"**

`python pdfwatermark.py -c "#FF0000" -o 0.3 -x 200 -y 150  -w "({})" -r "^(\d+).+$" -d meaning.pdf 42-file.pdf`

Puts a large transparent pink '(42)' at the given coordinates 
on the first page of the content of `42-file.pdf` and saves the resulting content
as `meaning.pdf` 
 

# Todo
* add a possibility to add watermarks on pages other than first
* make sure it works nicely with paper formats other than DIN A4
* handle (at least some) errors

 