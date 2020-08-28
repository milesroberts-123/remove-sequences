# remove-sequences

It is sometimes helpful, for purposes of comparison, to generate sequence files that complement other sequences files. Complement, in this context, is a term from [set theory](https://en.wikipedia.org/wiki/Complement_%28set_theory%29). Briefly, the complement of set A is will be a set B, such that all of the elements in set B are all of the elements in the sample space that are NOT included in set A.

## INPUT

1. A fasta file defining the entire sequence set you're working with (i.e. the sample space).
2. A fasta file containing the sequences you want to remove from the above file (i.e. the file you want the complement of)
3. A name for the output fasta file (i.e. the complement file)

## OUTPUT

A fasta formatted sequence file containing the sequences in file 1 minus the sequences in file 2.

## USAGE

For example, this code:

`python3 remove_sequences.py example_sequences.fasta example_subset.fasta example_output.fasta`

will take the sequences in `example_sequences.fasta`, remove the sequences in listed in `example_subset.fasta`, and save the results to `example_output.fasta`.

## DEPENDENCIES

I wrote this script in python v3.8 and it requires Biopython to run. Install Biopython with:

`pip install biopython`

## References

The code in this script was modified from [this BioStars post](https://www.biostars.org/p/4881/).

