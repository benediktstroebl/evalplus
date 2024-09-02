
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
    pass

assert get_max_triples(0) == 0
assert get_max_triples(1) == 0
assert get_max_triples(2) == 1
assert get_max_triples(3) == 2
assert get_max_triples(4) == 3
assert get_max_triples(5) == 6
assert get_max_triples(6) == 5
assert get_max_triples(7) == 5
assert get_max_triples(8) == 6
assert get_max_triples(9) == 6
assert get_max_triples(10) == 6
assert get_max_triples(11) == 8
assert get_max_triples(12) == 8
assert get_max_triples(13) == 8
assert get_max_triples(14) == 8
assert get_max_triples(15) == 8
assert get_max_triples(16) == 10
assert get_max_triples(17) == 10
assert get_max_triples(18) == 10
assert get_max_triples(19) == 10
assert get_max_triples(20) == 10
assert get_max_triples(21) == 12
assert get_max_triples(22) == 12
assert get_max_triples(23) == 12
assert get_max_triples(24) == 12
assert get_max_triples(25) == 12
assert get_max_triples(26) == 12
