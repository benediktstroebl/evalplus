
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
    # a = [1, 3, 7, 13, 21]
    # a = [3, 1, 21, 13, 7]
    a = [1, 21, 7, 3, 13]
    a = [3, 1, 7, 13, 21]
    # a = [3, 13, 1, 21, 7]
    # a = [3, 7, 1, 13, 21]
    # a = [13, 3, 1, 7, 21]

    # a = [1, 3, 7, 13, 21]
    # a = [1, 1, 1, 1, 1]
    # a = [3, 3, 3, 3, 3]
    # a = [7, 7, 7, 7, 7]
    # a = [13, 13, 13, 13, 
