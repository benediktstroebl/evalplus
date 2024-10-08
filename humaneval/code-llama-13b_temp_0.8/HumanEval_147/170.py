
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
    result = []
    a = [i*i - i + 1 for i in range(1, n+1)]
    a = sorted(a)
    for i in range(0, n-2):
        l = i + 1
        r = n - 1
        while l < r:
            s = a[i] + a[l] + a[r]
            if s % 3 == 0:
                result.append([a[i], a[l], a[r]])
                l += 1
                r -= 1
            elif s < 3:
                l += 1
            else:
                r -= 1
    return result

