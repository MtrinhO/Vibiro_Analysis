#Local application imports
genes= open(r"\Users\OWNER\3D Objects\BioinformaticsRepo\Vibrio\Vibrio_cholerae_DNASeq.txt",'r')
Genome = genes.read()
from DNATools import "genomic-k-mers.py"

#Inputs: Vibiro Cholera genome,k-mer, outputs dictionary of k-mers in genpme
Ori_Candidates = FrequentWords(Text=Genome,k=9)
print(Ori_Candidates)
#Input: keys from Ori_Candidates Output: positions of the 9-mers in the genome
Pattern_Matching(Text=Genome, Pattern="")
