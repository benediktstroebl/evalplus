
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
    # IMPORTANT: Finding the max number of triples is equivalent to finding the number
    # of indices for which the sum of the two numbers is a multiple of 3.
    # if the max number of triples is k, then we know that 2k + 1 < n
    # 
    # 2k + 1 < n
    # 2k + 1 = n
    # 2k + 1 - n = 0
    # 2k - n = 1
    # (2k - n) % 3 = 1
    # k % 3 = 2

    from math import sqrt
    if n < 3: return 0

    # 1) Start with the lowest number that has a square root as an integer
    # 2) Add 1 until the square root is no longer an integer
    # 3) Subtract 1 until the square root is an integer again
    # 4) Repeat steps 2) and 3) until square root is not an integer

    # 1) Start with the lowest number that has a square root as an integer
    # Find the lowest multiple of 3 that is greater than the square root of n
    max_triples = 0
    while (max_triples * max_triples) < n:
        max_triples += 1

    # 2) Add 1 until the square root is no longer an integer
    while (max_triples * max_triples) + 1 >= n:
        max_triples += 1

    # 3) Subtract 1 until the square root is an integer again
    while not ((max_triples * max_triples) + 1 == n):
        max_triples -= 1

    return max_triples

