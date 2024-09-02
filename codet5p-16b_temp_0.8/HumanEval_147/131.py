
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

    if not n:
        return 0
    a = [0] * n
    for i in range(n):
        a[i] = i*i - i + 1
    a.sort()
    res = 0
    for i in range(n-2):
        j, k = i+1, n-1
        while j < k:
            s = a[i] + a[j] + a[k]
            if s%3 == 0:
                res += 1
            if s > 0:
                k -= 1
            else:
                j += 1
    return res

