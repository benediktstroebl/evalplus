
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
    # No need to check if n is positive. it is already a positive number
    # n = 2 ** (n // 2)
    n = int(n)
    # n = 2 ** (n // 2)
    half = n // 2
    # n = 2 ** (n // 2)
    while half >= 1:
        # n = 2 ** (n // 2)
        if n % 2 == 0:
            # n = 2 ** (n // 2)
            even_count += 1
        # n = 2 ** (n // 2)
        half -= 1
    # n = 2 ** (n // 2)
    while half >= 0:
        # n = 2 ** (n // 2)
        if n % 2 != 0:
            # n = 2 ** (n // 2)
            odd_count += 1
        half += 1
    return (even_count, odd_count)
