def get_max_triples(n):
    # Create the sequence
    a = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum triples
    curr = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            curr = max(curr, sum(a[i:j+1]) // 3)
    return curr