
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
    # check if n is even or odd
    if n % 2 == 0:
        even = 0
    else:
        even = 1

    # check for remainder of n/2
    remainder = n // 2

    # check if remainder is even or odd
    if remainder % 2 == 0:
        odd = 0
    else:
        odd = 1

    # check for number of palindromes
    number_of_palindromes = (even + odd) // 2

    return number_of_palindromes
