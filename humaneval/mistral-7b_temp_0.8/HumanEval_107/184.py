
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
    # palindrome = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 101, 121, 131, 141, 151, 161, 171, 181, 191]
    # even_palindrome = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 102, 122, 142, 162, 182, 202, 222, 242, 262, 282, 302]
    # odd_palindrome = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 111, 131, 151, 171, 191, 211,
