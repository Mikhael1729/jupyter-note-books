import os
from Bio.Align.Applications import MuscleCommandline
import subprocess
from io import StringIO
from Bio import AlignIO, SeqIO

input_path = r"files\Secuencia_Nucleotideos.fasta"
output_path = r"output\output.txt"

# Neuclotids secuence
cline = MuscleCommandline(
  input=input_path,
  out=output_path
)

# Records
sequences = SeqIO.parse(input_path, "fasta")
records = (sequence for sequence in sequences if len(sequence) < 900)

# Muscle cline
muscle_cline = MuscleCommandline(clwstrict=True)

child = subprocess.Popen(
  str(cline),
  stdout = subprocess.PIPE,
  stderr = subprocess.PIPE,
  universal_newlines = True,
)

# Write the records
SeqIO.write(records, child.stdin, "fasta")
child.stdin.close()

# Get the stored records
align = AlignIO.read(child.stdout, "clustal")
print(align)

