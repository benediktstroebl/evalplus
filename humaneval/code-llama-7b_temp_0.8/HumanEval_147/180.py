
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
    # n = 5
    # a = [1, 3, 7, 13, 21]
    # [(1, 7, 13), (1, 7, 21), (3, 7, 13), (3, 7, 21), (1, 13, 21), (3, 13, 21)]

    return int(n*(n-1)*(n-2)/6)
