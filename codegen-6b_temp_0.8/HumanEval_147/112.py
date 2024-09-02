
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
    result = 0
    for i in range(1, n):
        for j in range(i, n):
            for k in range(j, n):
                if a[i] + a[j] + a[k] %3 == 0:
                    result += 1
    return result

assert get_max_triples(5) == 1
assert get_max_triples(7) == 3
assert get_max_triples(10) == 2
assert get_max_triples(32) == 3
assert get_max_triples(999) == 63
assert get_max_triples(1000) == 6
assert get_max_triples(10000) == 24
assert get_max_triples(99999) == 25