def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Initialize the count of triples
    max_triples = 0
    
    # Consider all possible pairs (a[i], a[j])
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Count triples where a[i], a[j], a[k] satisfies the condition
            max_triples += (a[j] - a[i] - 1) // 2 // 3 + 1
    
    return max_triples