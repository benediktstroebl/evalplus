def get_max_triples(n):
    a = [i * i - i + 1 for i in range(n)]
    return max([(a[i], a[j], a[k]) for j in range(i + 1) for i, j, k in range(n)])