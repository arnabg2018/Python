#!/lustre/work/apps/Anaconda3/python3

import os
from Bio import SeqIO
import statistics

RECORD = list(SeqIO.parse("NW-1.Trinity.fasta", "fasta"))
print("Total reads: %i" % len(RECORD))

sizes = [len(REC) for REC in SeqIO.parse("NW-1.Trinity.fasta", "fasta")]

print("Mean read length:", statistics.mean(sizes))
print("Median:", statistics.median(sizes))
print("Mode:", statistics.mode(sizes))
print("Max:", max(sizes))
print("Min:", min(sizes))
print()

generator = SeqIO.parse("NW-1.Trinity.fasta", "fasta")
print("Sample", "\t", "Read Length")

for SEQRECORD in generator:
	idkeep, rest = SEQRECORD.id.split(';',1)
	print(idkeep, "\t", len(SEQRECORD))