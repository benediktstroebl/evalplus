def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize counter for triples
    max_triples = 0
    
    # Consider all possible triples
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] >= 3: 
                    max_triples += 1
    
    return max_triples