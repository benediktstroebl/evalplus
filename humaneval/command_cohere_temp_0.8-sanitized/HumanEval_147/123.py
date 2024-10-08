def get_max_triples(n):
    arr = [i * i - i + 1 for i in range(1, n+1)]
    
    # Calculate occurrences 3 in arr[i] + arr[j] + arr[k]
    occ = [0 for _ in range(n*n)]
    occ[0] = arr[0]
    for i in range(1, n*n):
        occ[i] = occ[i - 1] + arr[i]
    occ = [occ[i] for i in range(n*n) if occ[i] >= 3]

    # Count occurrences (a[i], a[j], a[k])
    cnt = [0 for _ in range(n*n)]
    for i in range(n):
        for j in range(i + 1, n):
            k = (i + j) // 2
            if occ[arr[i] + arr[j] + arr[k]] >= 3:
                cnt[arr[i] + arr[j] + arr[k]] += 1

    return sum(cnt)