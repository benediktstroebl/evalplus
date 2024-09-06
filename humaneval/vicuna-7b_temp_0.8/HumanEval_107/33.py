
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
    # n = 0, return 0, 0, because there's no even and odd palindromes
    if n == 0:
        return 0, 0

    # calculate sum of digits of n
    num = sum(map(int, str(n)))

    # calculate number of even palindromes
    if num % 2 == 0:
        evens = 0
    else:
        evens = n // 2

    # calculate number of odd palindromes
    odds = (n + 1) // 2

    return evens, odds