
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
    """
        Time Complexity: O(N)
        Space Complexity: O(N)

    """
    mod = 3
    MOD = 10 ** 9 + 7
    res = 0
    if n > 2:
        for i in range(1, n):
            i_square = i * i - i + 1
            for j in range(i + 1, n):
                j_square = j * j - j + 1
                for k in range(j + 1, n):
                    k_square = k * k - k + 1
                    if (i_square + j_square + k_square) % mod == 0:
                        res += 1
    return res % MOD

