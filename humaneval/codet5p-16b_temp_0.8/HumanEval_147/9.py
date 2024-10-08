
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
    elif n == 3:
        return 1
    elif n == 4:
        return 2

    max_triple_count = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            max_triple_count += (i + j) % 3 == 0 and (i * i + j * j - i - j + 1) % 3 == 0

    return max_triple_count
