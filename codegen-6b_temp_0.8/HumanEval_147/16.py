
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
    n += 1
    a = [0] * n
    for i in range(1, n):
        a[i] = i * i - i + 1
    total = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if a[j] > a[i]:
                for k in range(j + 1, n):
                    if a[k] > a[i] and a[k] > a[j]:
                        total += 1
    return total

assert get_max_triples(5) == 1
assert get_max_triples(0) == 0
assert get_max_triples(1) == 1
assert get_max_triples(2) == 0
assert get_max_triples(3) == 1
assert get_max_triples(4) == 0
assert get_max_triples(10) == 3
assert get_max_triples(11) == 2
assert get_max_triples(100) == 46
