
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

    max_num = n * n
    final_count = 0
    for i in range(1, max_num):
        for j in range(i, max_num):
            for k in range(j, max_num):
                if i + j + k == 0:
                    pass
                if i + j + k % 3!= 0:
                    pass
                else:
                    final_count += 1

    return final_count
