#MODIFIED CODE FROM: https://www.biostars.org/p/4881/
import sys
from Bio import SeqIO
import re
print("Thanks for using this script!")
print("USAGE: python3 remove_sequences.py <INPUT SEQUENCE SET> <SEQUENCES TO REMOVE IN FASTA> <OUTPUT FASTA>")

#Parse inputs
input_file = sys.argv[1]  # Input fasta file
remove_file = sys.argv[2] # fasta file containing sequences to be removed from above file
output_file = sys.argv[3] # Output fasta file

#Build list of sequences in second fasta file, which will be removed from first fasta file
print("Building list of sequences to remove from %s ..." % input_file)
remove = set()
for record in SeqIO.parse(remove_file, "fasta"):
	remove.add(record.id)

#Omit sequences in first fasta file, based on list generated above
print("Removing sequences from %s ..." % input_file)
fasta_sequences = SeqIO.parse(input_file,"fasta")
with open(output_file, "w") as f:
	for record in fasta_sequences:
		id = record.id
		if id not in remove:
			SeqIO.write(record, f, "fasta")
print("Removal complete!")
