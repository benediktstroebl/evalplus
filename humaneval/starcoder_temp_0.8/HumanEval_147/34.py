
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
    def count(x):
        return x * (x + 1) * (x + 2) // 6
    
    def solve(n, m):
        return (n * (n + 1) // 2 - sum(x <= m for x in a)) // 3
    
    a = [i * i - i + 1 for i in range(1, n + 1)]
    x = 0
    for m in range(1, n + 1):
        x = max(x, solve(n, m))
    return x
