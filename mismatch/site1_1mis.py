seq = "AGAGCCCCAGAGACCGGCAC"


length = len(seq)   

def mutate(base):   
    assert base in ['A', 'T', 'C', 'G']    
    if base == 'A': 
        return ['T', 'C', 'G']  
    elif base == 'T':
        return ['A', 'C', 'G']
    elif base == 'C':
        return ['A', 'T', 'G']
    else:
        return ['A', 'T', 'C']

for i in range(length - 1):     
    for i2 in mutate(seq[i]):
        
        print ('\t'.join(list(seq[:i] + i2 + seq[i+1:])))

