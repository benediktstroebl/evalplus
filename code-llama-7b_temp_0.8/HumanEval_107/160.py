
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
    if n < 1:
        raise ValueError('n must be >= 1.')

    evens = 1 if n % 2 == 0 else 0
    odds = 1 if n % 2 else 0

    for i in range(n - 1):
        even = evens + i % 2
        odd = odds + 1 - i % 2

        if even % 2 and odd % 2:
            break

        evens, odds = odd, even

    return evens, odds
