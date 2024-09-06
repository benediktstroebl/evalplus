
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
    a = [i*i*i - i*i + 1 for i in range(n)]
    n = max(a)
    return n

print(get_max_triples(5))  # 1
print(get_max_triples(6))  # 2
print(get_max_triples(7))  # 1
print(get_max_triples(8))  # 2
print(get_max_triples(9))  # 1
print(get_max_triples(10))  # 2
print(get_max_triples(11))  # 1
print(get_max_triples(12))  # 2