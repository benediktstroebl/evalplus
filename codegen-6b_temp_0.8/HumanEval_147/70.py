
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
    def build(n, lower_limit):
        if n == 0:
            return []
        elif n == 1:
            return [(0, 0, 1)]
        elif n == 2:
            return [(0, 0, 0), (0, 1, 1), (1, 1, 2), (1, 0, 1)]
        elif n == 3:
            return [(0, 0, 0), (0, 1, 1), (0, 2, 2), (1, 1, 1), (1, 2, 1), (2, 2, 1), (2, 1, 2)]
        else:
            return build(n-1, 2) + \
                   [(3*item1+2*item2, item1+item2+item3, item1+item2+item3+1) for item1 in build(n-2, 1) for item2 in build(n-2, 1) for item3 in build(n-2, 1)] + \
                   [(item1+item2+item3, item1+item2+item3, item1+item2+item3+1) for item1 in build(n-3, 1) for item2 in build(n-3, 1) for item3 in build(n-3, 1)] 
    return len([triple for triple in build(n, 1) if sum(triple) % 3 == 0]) // 3
