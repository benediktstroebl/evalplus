def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize a count for the triples
    max_triples = 0
    
    # Loop through all combinations of 3 indices
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] >= 3:
                    max_triples += 1
    
    return max_triples