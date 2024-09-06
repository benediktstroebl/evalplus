def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate the maximum triples
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            current_sum = a[i] + a[j]
            max_triples = max(max_triples, len(list(filter(lambda x: x == current_sum, [a[k] for k in range(n) ]))))
    return max_triples