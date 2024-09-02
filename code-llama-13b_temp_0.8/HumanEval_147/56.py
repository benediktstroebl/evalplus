
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
    mod_list = {}
    for i in range(1, n):
        for j in range(i+1, n):
            total = a[i] + a[j]
            if total % 3 == 0:
                k = total // 3
                if k in mod_list and mod_list[k] < j:
                    return 1
            mod_list[total % 3] = j
    return 0

