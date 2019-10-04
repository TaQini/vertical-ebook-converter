Vertical-Ebook-Converter
========================
python based software to convert Amazon / Kindlegen generated ebooks to vertical style

based on https://github.com/kevinhendricks/KindleUnpack

## usage
download kindlegen and copy it to your system path 
```
$ wget http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz
$ tar xvf ./kindlegen_linux_2.6_i386_v2_9.tar.gz 
$ sudo cp ./kindlegen /usr/bin
```

check if kindlegen work
```
$ kindlegen

*************************************************************
 Amazon kindlegen(Linux) V2.9 build 1028-0897292 
 A command line e-book compiler 
 Copyright Amazon.com and its Affiliates 2014 
*************************************************************

Usage : kindlegen [filename.opf/.htm/.html/.epub/.zip or directory] [-c0 or -c1 or c2] [-verbose] [-western] [-o <file name>] 

...
```

then 
```
$ ./kindleConverter infile [outfile]
```

## works
### modify content.opf
```html
<dc:language>zh-tw</dc:language>
<meta name="primary-writing-mode" content="vertical-rl" />
```

### modify CSS file
```css
body {
	margin: 5%;
	text-align: justify;
	-webkit-writing-mode: vertical-rl;
}
```

### replace quot.
 - ‘ -> 『
 - ’ ->  』
 - “ -> 「
 - ” ->  」

### reference
https://bookfere.com/post/204.html
https://bookfere.com/post/92.html#kg
