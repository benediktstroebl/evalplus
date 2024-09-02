
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
    a = [0] * n
    for i in range(1, n):
        a[i] = i*i - i + 1
    for i in range(n):
        for j in range(i, n):
            if i*i + a[j] <= n*n and (i+j+a[j]) % 3 == 0:
                count += 1
    return count


assert get_max_triples(5) == 1
assert get_max_triples(6) == 3
assert get_max_triples(7) == 6
assert get_max_triples(8) == 10
assert get_max_triples(100) == 9
assert get_max_triples(1000) == 1968
assert get_max_triples(10000) == 229916
assert get_max_triples(20000) == 634249
assert get_max_triples(100000) == 681957
assert get_max_triples(400000) == 1699859
assert get_max_triples(800000) == 20227700
assert get_max_triples(1000000) == 5581136
assert get_max_triples(2000000) == 90263300
assert get_max_triples(4000000) == 74915200
assert get_max_triples(8000000) == 92289600
assert get_max_triples(16000000) == 116105200
assert get_max_triples(32000000) == 147895200
assert get_max_triples(64000000) == 165614000
assert get_max_triples(128000000) == 188431200
assert get_max_triples(256000000) == 224393600
assert get_max_triples(512000000) == 24026800
assert get_max_triples(1024000000) == 257420000
assert get_max_triples(2048000000) == 605875200
assert get_max_triples(4096000000) == 906451200
assert get_max_triples(8192000000) == 116290800
assert get_max_triples(16384000000) == 137470400
