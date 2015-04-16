# ParsingScript
Used to parse PDFs found in: http://www.mapress.com/zootaxa/list/2011/3148.html

Simple parsing script that is used to parse phylogenies in PDF format in the website linked above.
To run the parser simply:

./parse_file.py phylogenyName.txt

The output will result in a "parsed.txt" file with the phylogeny organized as follows:
TaxonomicLevel  TaxonmicName  Order/Family/Genus/Species Number

The use of this parser was used during a BOLD project to update all phylogenies within the system.
