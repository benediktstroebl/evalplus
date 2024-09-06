
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
    if n <= 3:
        return 0
    if n == 4:
        return 1
    a = [0] * n
    a[1] = 1
    a[2] = 2
    for i in xrange(3, n):
        a[i] = i * i - i + 1
    actual = 0
    for i in xrange(n):
        for j in xrange(i):
            for k in xrange(j):
                actual += a[i] * a[j] * a[k]
                if actual % 3 == 0:
                    return actual / 3
    return actual / 3


assert 4 == get_max_triples(4)
assert 1 == get_max_triples(5)
assert 0 == get_max_triples(6)
assert 1 == get_max_triples(7)
assert 6 == get_max_triples(8)
assert 9 == get_max_triples(15)
assert 105 == get_max_triples(22)
assert 56 == get_max_triples(29)
assert 156 == get_max_triples(34)
