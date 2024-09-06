def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    # triples that sum up to a multiple of 3
    triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            total = arr[i] + arr[j] + arr[j + 1]
            if total % 3 == 0:
                triples += 1
    return triples