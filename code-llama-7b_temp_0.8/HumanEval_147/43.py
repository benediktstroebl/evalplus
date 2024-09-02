
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

    # Time Complexity: O(N)
    # Space Complexity: O(1)
    # n = 5
    # i * i - i + 1 = i * (i - 1) + 1 = 3k + 1
    # all the number will be multiple of 3

    # Explanation
    # (a[i], a[j], a[k]) = (i * i - i + 1, j * j - j + 1, k * k - k + 1)
    # i + j + k = 3k + 3
    # i + j + k = 3k + 1 + 2 + 1
    # i + j + k = 3k + 3 + 1
    # i + j + k = 3k + 3 + 3
    # i + j + k = 3k + 9
    # i + j + k = 3(k + 3)
    # So i, j, k should be 3 and 3, 6 and 6, ...
    # a = [1, 4, 9, 16, 25]
    # a = [1, 3, 7, 13, 21]
    # a = [1, 3, 7, 13, 21, 30, 38, 48, 58, 69, 81, 94]
    # 1 + 4 + 9 = 14
    # 1 + 7 + 16 = 24
    # 1 + 13 + 25 = 39
    # 24 + 24 + 24 = 72
    # 24 + 30 + 38 = 100
    # 39 + 48 + 58 = 127
    # 39 + 69 + 81 = 189

    res = 0

    # Since 3 * 3 - 3 + 1 = 9
    # a[i] % 3 == 0
    # a[
