
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
    even, odd = 0, 0
    n, r = n, n
    while n > 0:
        n, m = divmod(n, 10)
        r = 10 * r + m
    while r > 0:
        r, m = divmod(r, 10)
        if r == m:
            if r % 2 == 0:
                even += 1
            else:
                odd += 1
        else:
            return even, odd
    return even, odd
