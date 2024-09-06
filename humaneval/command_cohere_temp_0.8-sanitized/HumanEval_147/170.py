def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate maximum triples
    max_triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            curr_sum = a[i] + a[j]
            max_triples += (curr_sum // 3) * (curr_sum // 3 + 1)
    return max_triples