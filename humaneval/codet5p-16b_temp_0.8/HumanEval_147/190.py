
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

    from collections import defaultdict
    res = 0
    mod_3 = defaultdict(int)
    mod_3[0] = 1
    mod_3[3] = 1
    mod_3[6] = 1
    for i in range(1, n+1):
        for j in range(i, n+1):
            res += mod_3[i*i - i + 1]
            res += mod_3[j*j - j + 1]
            res += mod_3[i*j*(i+j)//3]
            mod_3[i*i - i + 1] += 1
            mod_3[j*j - j + 1] += 1
            mod_3[i*j*(i+j)//3] += 1
    return res

