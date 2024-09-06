
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
    def get_valid_triples(n, curr):
        if n == 1:
            yield (curr, )
            return
        for i in range(curr + 1, n):
            for a in get_valid_triples(n - 1, i):
                yield (i, ) + a
    
    return count_of_triples(get_valid_triples(n, 0))
