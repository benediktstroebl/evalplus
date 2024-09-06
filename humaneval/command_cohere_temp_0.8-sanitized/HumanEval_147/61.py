def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate max triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            curr = a[i] + a[j]
            remaining = 3 - (curr % 3)
            max_triples = max(max_triples, remaining)
    return max_triples