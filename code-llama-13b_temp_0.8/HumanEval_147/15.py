
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
    # Time complexity O(N) and space O(N)
    mod = 3
    triples = 0
    count = [0] * n
    for i in range(n):
        count[i] = count[i - 1] if i > 0 else 0
        count[i] += (a[i]%mod == 0)
    for j in range(n):
        for k in range(j+1, n):
            if (a[j] + a[k]) % mod == 0:
                triples += count[k - 1] if j > 0 else 0
    return triples
