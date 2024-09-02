
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
    if n == 1:
        return 1
    n = n - 1
    x = n // 2
    y = n // 3
    z = n // 6
    if x * 3 + y * 2 + z == n:
        return 1
    elif x * 3 + y * 2 + z > n:
        return 0
    else:
        return get_max_triples(n - x - y - z) + 1

    # get_max_triples(5)

