
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
    a = [i*i - i + 1 for i in range(1, n+1)]
    ans = 0
    i = 0
    j = 1
    k = 2
    while k < n:
        if (a[i] + a[j] + a[k])%3 == 0:
            ans += 1
        # moving j
        while (j < n and (a[i] + a[j] + a[k])%3 != 0):
            j += 1
        # moving k
        while (k < n and (a[i] + a[j] + a[k])%3 != 0):
            k += 1
        # decreasing j
        while (j > i+1 and (a[i] + a[j] + a[k])%3 != 0):
            j -= 1
        # decreasing k
        while (k > j+1 and (a[i] + a[j] + a[k])%3 != 0):
            k -= 1
        # moving i
        i += 1
        j += 1
        k += 1
    return ans

