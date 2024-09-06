
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
    l = [i * i - i + 1 for i in range(1, n + 1)]
    print(l)
    result = 0
    l_3 = [i for i in l if i % 3 == 0]
    for i in range(len(l_3)):
        for j in range(i + 1, len(l_3)):
            for k in range(j + 1, len(l_3)):
                if (l_3[i] + l_3[j] + l_3[k]) % 3 == 0:
                    result += 1
    return result

