
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
    a = [i * i - i + 1 for i in range(1, n + 1)]
    return sum(a[i] > sum(a[:i]) for i in range(3, n + 1))


assert get_max_triples(5) == 1
assert get_max_triples(10) == 3
assert get_max_triples(15) == 6
assert get_max_triples(20) == 10
assert get_max_triples(25) == 13
assert get_max_triples(50) == 24
assert get_max_triples(100) == 49
assert get_max_triples(200) == 98
assert get_max_triples(300) == 121
assert get_max_triples(400) == 162
assert get_max_triples(500) == 185
assert get_max_triples(600) == 216
assert get_max_triples(700) == 243
assert get_max_triples(800) == 266
assert get_max_triples(900) == 282
assert get_max_triples(1000) == 286
assert get_max_triples(2000) == 583
assert get_max_triples(3001) == 630
assert get_max_triples(4000) == 1032
assert get_max_triples(5000) == 1472
assert get_max_triples(6000) == 1815
assert get_max_triples(7000) == 2466
assert get_max_triples(8000) == 3081
assert get_max_triples(9000) == 3629
assert get_max_triples(10000) == 4590
assert get_max_triples(25000) == 4706
assert get_max_triples(50000) == 4538
assert get_max_triples(600000) == 4666
assert get_max_triples(7000000) == 4624
assert get_max_triples(8000000) == 4620
assert get_max_triples(9000000) == 4595
assert get_max_triples(10000000) == 4540
assert get_max_triples(1500000) == 4527
assert get_max