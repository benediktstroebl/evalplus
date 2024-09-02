
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
    assert n >= 1

    # NOTE: using the fact that all numbers from 1 to n are the sum of two
    # squares (and hence of three), a[i] is always of the form (i^2 - i + 1), 
    # i.e., a[i] = i * i - i + 1.
    #
    # The sum of three numbers (a[i], a[j], a[k]) is a multiple of 3 if and
    # only if each of the numbers a[i], a[j], and a[k] is a multiple of 3, or
    # if the sum of any two of a[i], a[j], and a[k] is a multiple of 3.
    #
    # Let's call an integer a[i], and the sum of two other integers
    # a[j] and a[k] containing it, a "substring". 

    # For each integer i, let's count how many different substring-pairs 
    # containing it exist.
    #
    # 0 <= i < n
    # 1 <= j < k <= n
    # a[i] = i * i - i + 1
    # a[j] = j * j - j + 1
    # a[k] = k * k - k + 1
    # a[j] + a[k] = (j * (j - 1) + k * (k - 1)) / 2
    # 
    # Let's assume that the sum of two numbers containing some number a[i] is
    # a multiple of 3: a[j] + a[k] = 3 * q.
    # Then, (a[j] - a[i] + 1) and (a[k] - a[i] + 1) have to be a multiple of 3,
    # too, since they are equal to j * (j - 1) / 2 and k * (k - 1) / 2, respectively.
    # This implies that (j - i) and (k - i) are multiples of 3, i.e., 
    # either 0,
