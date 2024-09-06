
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
    def helper(a, i, n):
        if i == n:
            return 1
        else:
            return helper(a, i + 1, n) + (a[i] + helper(a, i + 1, n)) * (i + 1)

    a = []
    for i in range(n):
        a.append((i + 1) ** 2 - i + 1)

    return helper(a, 0, n)

