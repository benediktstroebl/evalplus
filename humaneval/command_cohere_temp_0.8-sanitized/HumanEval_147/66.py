def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize the count of triples
    triples = 0
    
    # Calculate valid triples and count them
    for i in range(n-2):
        for j in range(i+1, n-1):
            if (a[i] + a[j] + a[j+1]) % 3 == 0:
                triples += 1
    
    return triples