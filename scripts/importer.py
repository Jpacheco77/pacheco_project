import dendropy

amphib = dendropy.DnaCharacterMatrix.get(
    path="../data/plethodon.phy",
    schema="newick"
)

amphib.write_to_path("../data/plethodon.fa", schema="fasta")