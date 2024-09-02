
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
    # How to get the number of integers that are multiples of 3 and that can be expressed as 1+2+...+k 
    # where k is an integer (0 <= k <= 2) ? 
    # For example, (1, 1, 1) is a triple that can be expressed as 1+1+1 = 3, which is a multiple of 3.
    # The solution is just the number of integers that are multiples of 3, which is exactly n // 3.
    return n // 3
