
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
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    if n < 10:
        return 0, 0
    elif n == 10:
        return 1, 1
    elif is_palindrome(n):
        return 1, 0
    elif n % 2 == 0:
        return even_odd_palindrome(n - 1)
    else:
        return even_odd_palindrome(n - 1) + 1, even_odd_palindrome(n - 1)

