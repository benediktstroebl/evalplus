
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
    
    a = [x for x in range(1, int(n))]
    count = 0
    
    for i in a:
        for j in a:
            if i < j:
                for k in a:
                    if i < k < j:
                        if i + j + k == 3 * ((i ** 2) + (j ** 2) + (k ** 2)):
                            count += 1
    
    return count

assert get_max_triples(3) == 0
assert get_max_triples(2) == 1
assert get_max_triples(5) == 3
assert get_max_triples(6) == 6
assert get_max_triples(7) == 4