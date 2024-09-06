def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate counter for each number and its pairs
    cnt = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] >= 3:
                cnt[i] += 1
                cnt[j] += 1

    # Calculate max triples through triple counting
    max_triples = 0
    for i in range(n):
        max_triples += cnt[i] // 2
        # For each number, its pairs can contribute at most 4 triples
        # (since for every pair, the number itself is also a multiple of 3)
        max_triples = max(max_triples, 4 - cnt[i] // 2)
    
    return max_triples