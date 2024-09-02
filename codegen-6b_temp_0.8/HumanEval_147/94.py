
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
    count = 0
    n1 = n
    while n1 % 3 == 0:
        count += n1 // 3
        n1 //= 3
    n1 = n
    while n1 % 5 == 0:
        count += n1 // 5
        n1 //= 5
    if n1 % 7 == 0:
        count += n1 // 7
    return count


assert get_max_triples(5) == 1
assert get_max_triples(10) == 2
assert get_max_triples(15) == 3
assert get_max_triples(20) == 5
assert get_max_triples(25) == 8
assert get_max_triples(30) == 14
assert get_max_triples(35) == 17
assert get_max_triples(40) == 22
assert get_max_triples(45) == 25
assert get_max_triples(50) == 43
assert get_max_triples(55) == 50
assert get_max_triples(60) == 58
assert get_max_triples(65) == 64
assert get_max_triples(70) == 72
