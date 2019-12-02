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

for i in range(length - 2):     
    for j in range(i+1,length-1):
        for k in range(j+1,length):

            for k2 in mutate(seq[k]):
                for j2 in mutate(seq[j]):
                    for i2 in mutate(seq[i]):
                        print ('\t'.join(list(seq[:i] + i2 + seq[i+1:j] + j2 + seq[j+1:k] + k2 + seq[k+1:])))