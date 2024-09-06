
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
    from functools import reduce
    if n < 3:
        return 0
    n1, n2, n3 = 0, 0, 0
    max = n*(n-1)*(n-2)//6
    for i in range(3, n+1):
        if max < 0:
            break
        n1 = i*(i-1)*(i-2)//6
        n2 = reduce(lambda x, y: x+y, range(i, n+1, i), 0)
        n3 = reduce(lambda x, y: x+y, range(i, n+1, i*i-i+1), 0)
        max -= (n1+n2+n3)//3
    return max

