def get_max_triples(n):
    a = [i for i in range(n+1)]
    a[0] = 1
    a[1] = 3
    a[n] = 21
    for i in range(n):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if a[i] + a[j] + a[k] > 3:
                    return 1
    return 0