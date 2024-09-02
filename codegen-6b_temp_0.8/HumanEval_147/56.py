
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
    from math import sqrt
    max_triples = 0

    for a in xrange(0, n):
        a *= a
        for b in xrange(a, n):
            b *= b
            c = (a + b) / 3
            if c % 1 == 0 and c != int(c):
                max_triples += 1
    return max_triples

assert get_max_triples(5) == 1
assert get_max_triples(10) == 2
assert get_max_triples(20) == 3
assert get_max_triples(100) == 22
assert get_max_triples(1000) == 233
assert get_max_triples(10000) == 23308
assert get_max_triples(100000) == 2333043