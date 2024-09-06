def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    triples = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] + arr[j-i-1]) % 3 == 0:
                triples += 1
    return triples