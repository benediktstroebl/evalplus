
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
    even_cnt = 0
    odd_cnt = 0
    even = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    odd = [1, 3, 5, 7, 9]
    n = n - 1
    for i in range(0, 5):
        if n >= pow(10, 2 * i + 1):
            if (i + 1) % 2 == 0:
                even_cnt += min(10 - 1, n // pow(10, 2 * i + 1))
            else:
                odd_cnt += min(10 - 1, n // pow(10, 2 * i + 1))
    for i in range(0, len(even)):
        if n >= pow(10, 2 * i):
            even_cnt += min(10 - i - 1, n // pow(10, 2 * i))
    for i in range(0, len(odd)):
        if n >= pow(10, 2 * i + 1):
            odd_cnt += min(10 - i - 1, n // pow(10, 2 * i + 1))
    return (even_cnt, odd_cnt)

