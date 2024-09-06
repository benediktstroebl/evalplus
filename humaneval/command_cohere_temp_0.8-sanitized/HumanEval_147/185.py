def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Calculate max triples through prefix sum
    ps = [0] * (n + 1)
    for ai in a:
        ps[ai] += 1

    max_triples = 0
    for i in range(1, n + 1):
        max_triples = max(max_triples, ps[i] - ps[i - 1] - ps[i + 1])
    
    return max_triples