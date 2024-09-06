def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            current_sum = a[i] + a[j]
            triples = (current_sum - 1) // 3
            max_triples = max(max_triples, triples)
    return max_triples