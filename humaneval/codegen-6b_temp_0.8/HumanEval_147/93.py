
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
    a = [i * i - i + 1 for i in range(n)]
    return sum([1 for i in range(n) for j in range(i) for k in range(j, n) if (a[i] + a[j] + a[k]) % 3 == 0])

assert get_max_triples(5) == 1
assert get_max_triples(50) == 9
assert get_max_triples(500) == 55
assert get_max_triples(1001) == 576
assert get_max_triples(0) == 0

