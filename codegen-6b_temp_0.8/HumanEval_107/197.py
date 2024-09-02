
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
        if n == 0 or n == 1:
            return True
        return n % 10 == n // 10

    return (is_palindrome(n + 1), is_palindrome(n))


assert even_odd_palindrome(3) == (1, 2)
assert even_odd_palindrome(12) == (4, 6)
assert even_odd_palindrome(0) == (1, 0)
assert even_odd_palindrome(1) == (1, 0)
assert even_odd_palindrome(10) == (0, 2)
assert even_odd_palindrome(999) == (1, 1)
assert even_odd_palindrome(9990) == (1, 2)
assert even_odd_palindrome(1234) == (0, 1)
assert even_odd_palindrome(11111) == (2, 1)
