#!/lustre/work/apps/Anaconda3/python3

import os
from Bio import SeqIO

input_file = open('NW-1.Trinity.fasta', 'r')
output_file = open('basepair_counts.tsv','w') 
output_file.write('Gene\tA\tC\tG\tT\tLength\n')

for RECORD in SeqIO.parse(input_file, "fasta") :

## Counting base pairs (nucleotides) in this record ##

	GENE_ID = RECORD.name
	A_count = RECORD.seq.count('A')
	C_count = RECORD.seq.count('C')
	G_count = RECORD.seq.count('G')
	T_count = RECORD.seq.count('T')

	LENGTH = len(RECORD.seq) 
	output_line = '%s\t%i\t%i\t%i\t%i\t%i\n' %  (GENE_ID, A_count, C_count, G_count, T_count, LENGTH)
	output_file.write(output_line)
output_file.close()
input_file.close()   