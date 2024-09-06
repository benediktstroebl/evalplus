def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    # Calculate the maximum number of triples
    max_triples = sum(1 for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n) if arr[i] + arr[j] + arr[k] % 3 == 0)
    return max_triples