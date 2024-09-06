
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
    a = [0] * n
    multiple_of_3 = False

    for i in range(1, n):
        a[i] = i * i - i + 1

        if a[i] % 3 == 0:
            multiple_of_3 = True
    
    return a[0] if multiple_of_3 else 0

assert get_max_triples(5) == 1
assert get_max_triples(10) == 2
assert get_max_triples(25) == 3
assert get_max_triples(100) == 12

