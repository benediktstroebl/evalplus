
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    def odd_even(x, k):
        res = 0
        while x:
            k, res = res * 10 + x % 10, k * 10 + x % 10
            x //= 10
        return k, res

    res = 0
    for i in range(1, n + 1):
        k, r = odd_even(i, i)
        if k > r and k - r in range(1, n + 1):
            res += 1

    return res // 2, res % 2

