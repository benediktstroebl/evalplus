
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
    def power(x, y):
        if y == 0:
            return 1
        elif y == 1:
            return x
        else:
            return x * power(x, y - 1)
    return power(3, n) // 2

assert get_max_triples(5) == 1
assert get_max_triples(3) == 0
assert get_max_triples(4) == 0
assert get_max_triples(8) == 0


get_max_triples = lambda n : sum(i for i in range(1, n + 1) for j in range(i + 1, n + 1) for k in range(j + 1, n + 1) if (i * i + j * j + k * k) % 3 == 0)
