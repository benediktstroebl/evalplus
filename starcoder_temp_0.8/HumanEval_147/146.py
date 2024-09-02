
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    def check_triple(a, i, j, k):
        return a[i] + a[j] + a[k] % 3 == 0
    
    a = [None] * n
    i = 1
    while i * i <= n:
        j = 1
        while i * j <= n:
            k = n // i // j
            a[k] = i * j
            j += 1
        i += 1
    res = 0
    for i in range(n):
        if a[i] is None: continue
        for j in range(i + 1, n):
            if a[j] is None: continue
            k = a[i] + a[j]
            if k > n: break
            if check_triple(a, i, j, k):
                res += 1
    return res
