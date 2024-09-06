def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible triples
    for i in range(n-2):
        for j in range(i+1, n-1):
            k = range(j+1, n)
            rem = a[i] + a[j] + a[k[0]]
            if rem % 3 == 0:
                max_triples += 1
    
    return max_triples