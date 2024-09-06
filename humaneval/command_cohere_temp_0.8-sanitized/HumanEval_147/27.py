def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate the maximum number of triples per line
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sum_of_triples = arr[i] + arr[j] + arr[j + 1]
            max_triples = max(max_triples, sum_of_triples // 3)
    
    return max_triples