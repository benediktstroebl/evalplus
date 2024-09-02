
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
        return 0
    if n == 2:
        return 1
    a = [1]
    a.extend([ i * i - i + 1 for i in range(2, n)])
    max_triples = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] % 3 == 0:
                    max_triples += 1
    return max_triples

assert get_max_triples(1) == 0
assert get_max_triples(2) == 1
assert get_max_triples(3) == 1
assert get_max_triples(4) == 2
assert get_max_triples(5) == 2
assert get_max_triples(6) == 3
assert get_max_triples(7) == 4
assert get_max_triples(8) == 5
assert get_max_triples(9) == 6
assert get_max_triples(10) == 7
assert get_max_triples(11) == 8
assert get_max_triples(12) == 8
assert get_max_triples(13) == 9
assert get_max_triples(14) == 9
assert get_max_triples(15) == 10
assert get_max_triples(16) == 10
assert get_max_triples(17) == 11
assert get_max_triples(18) == 11
assert get_max_triples(19) == 12
assert get_max_triples(20) == 12
assert get_max_triples(21) == 13
assert get_max_triples(22) == 13
assert get_max_triples(23) == 13
assert get_max_triples(24) == 14
assert get_max_triples(25) == 14
assert get_max_triples(26) == 15
assert get_max_triples(27) == 16
assert get_max_triples(28) == 17