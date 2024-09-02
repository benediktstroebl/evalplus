
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
    # [1, 3, 7, 13, 21]
    # (a[i], a[j], a[k])
    # (1, 7, 13)
    # a[i] + a[j] + a[k] is a multiple of 3
    # a[i] - a[j] + a[k] is a multiple of 3
    # (a[i] + a[j] + a[k]) / 3 * 3 = 3a[i] - a[j] + a[k]
    # 3a[i] - a[j] + a[k] = a[i] + a[j] + a[k]
    # 3a[i] - a[j] = a[i] + a[j] + a[k] - a[k]
    # 3a[i] - a[j] = 3a[i] - 3a[k] + a[k]
    # 3a[i] = 3a[k] - a[j] + a[k]
    # 3a[i] = 3a[k] - a[j]
    # a[i] = 1/3 * (3a[k] - a[j])
    # (1/3) * (3a[k] - a[j]) + a[j]
    # [1, 3, 7, 13, 21]
    # (1, 7, 13)
    # 3 * (1, 7, 13) = 3a[i]
    # 3a[i] = 1 + 3 + 9 + 27
    # 3a[i] = 37
    # a[i] = 37 / 3 = 12
    # 
    # a = [12, 12, 12, 12, 12]
    # (12, 12, 12)
    # 3a[i] = 12 + 12 + 12 + 12 + 
