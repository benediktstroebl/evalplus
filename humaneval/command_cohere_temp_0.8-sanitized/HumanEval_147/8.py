def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Initialize the count of triples
    triples = 0
    
    # Calculate the number of triples for values greater than or equal to 3
    for i in range(3, n + 1, 3):
        for j in range(i + 1, n + 1, 3):
            k = (i + j) // 2
            if k >= 1 and a[k - 1] == 2:
                triples += 1
    
    return triples