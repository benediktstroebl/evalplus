
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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] + a[j] + a[j] > 3 * a[i]:
                count += 1
    return count


assert get_max_triples(5) == 1
assert get_max_triples(4) == 0
assert get_max_triples(3) == 0
assert get_max_triples(2) == 0
assert get_max_triples(1) == 0
assert get_max_triples(0) == 0
assert get_max_triples(100) == 0
assert get_max_triples(101) == 1
assert get_max_triples(102) == 0
assert get_max_triples(103) == 1
assert get_max_triples(201) == 1
assert get_max_triples(202) == 0
assert get_max_triples(1000) == 2