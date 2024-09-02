
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

    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    mod = 3
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            if (a[i] + a[left] + a[right]) % mod == 0:
                count += 1
                left += 1
                right -= 1
            elif (a[i] + a[left] + a[right]) % mod > 0:
                left += 1
            else:
                right -= 1
    return count

