
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
    ans = 0
    for i in range(1, n):
        l = i
        r = n
        while l < r:
            mid = (l+r) >> 1
            if mid * mid - mid + 1 + i * i - i + 1 + mid * mid - mid + 1  % 3 == 0:
                ans += r-l
                l += 1
            elif mid * mid - mid + 1 + i * i - i + 1 + mid * mid - mid + 1  < 0:
                l += 1
            else:
                r -= 1
    return ans

