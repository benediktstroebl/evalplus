def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate maximum triples
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j] + a[j-i-1]) % 3 == 0:
                triples += 1
    return triples