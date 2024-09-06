
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
    # Input is the length of the input range
    if n < 1:
        return 0, 0
    if n == 1:
        return 0, 1
    if n == 2:
        return 1, 1
    if n == 3:
        return 1, 2

    # The number of palindromes are the sum of the number of even and odd palindromes
    even = odd = 0
    for i in range(n - 1):
        even += i // 2
        odd += i // 2 + 1
    return even, odd
