'''
pip install pubchempy
'''

import pubchempy as pcp 

# Define the chemical formula of the hydrocarbon
chemical_formula = input("Enter chemical formula: ")
try:
    # Search PubChem for the compound by its chemical formula
    compound = pcp.get_compounds(chemical_formula, 'formula')[0]

    # Display information about the compound
    print(f"Name: {compound.iupac_name}")
    print(f"Common Name: {compound.synonyms[0]}")
    print(f"Molecular Weight: {compound.molecular_weight}")
    print(f"Formula: {compound.molecular_formula}")
    
    # You can access more properties as needed
except IndexError:
    print(f"No information found for {chemical_formula}. Please check Formula.")
