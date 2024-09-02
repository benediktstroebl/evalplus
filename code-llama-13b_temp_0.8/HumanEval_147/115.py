
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
    def isMultiple(a, b, c):
        return (a + b + c) % 3 == 0
    
    def find_j_and_k(n, i):
        j, k = 0, 0
        while j < n and j < i:
            if i * i - i + 1 + j * j - j + 1 + k * k - k + 1 != 0 and (i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 == 0:
                return j, k
            k += 1
            if k >= n:
                j += 1
                k = j + 1

    n_triples = 0
    a = []
    for i in range(1, n + 1):
        a.append(i * i - i + 1)
        j, k = find_j_and_k(n, i)
        if j == 0 and k == 0:
            continue
        n_triples += k - j
    return n_triples



