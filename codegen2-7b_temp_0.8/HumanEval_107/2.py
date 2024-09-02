
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
    def even_odd(n):
        if n == 1:
            return (1, 1)
        elif n % 2 == 0:
            return (n // 2, n // 2)
        else:
            return (n // 2 + 1, n // 2 + 1)

    return tuple(filter(lambda x: x >= 1 and x <= n, map(even_odd, range(1, n + 1))))

