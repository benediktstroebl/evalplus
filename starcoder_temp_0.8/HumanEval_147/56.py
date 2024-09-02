
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
    if n < 3:
        return 0
    mod = 3
    i = 0
    j = 0
    k = 1
    count = 0
    while k < n:
        a = (i * i - i + 1) % mod
        b = (j * j - j + 1) % mod
        c = (k * k - k + 1) % mod
        count += (a + b + c) % mod == 0
        if k == j:
            j += 1
        else:
            i = j
            j = k
        k += 1
    return count
