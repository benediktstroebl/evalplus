
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

    def get_all_triples(n):
        i = 1
        while i < n:
            for j in range(i, n):
                k = n - j + 1
                yield (i, j, k)
            i += 1
    count = 0
    for i, j, k in get_all_triples(n):
        if (i + j + k) % 3 == 0:
            count += 1
    return count
