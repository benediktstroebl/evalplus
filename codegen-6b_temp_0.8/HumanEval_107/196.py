
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
    evens, odds = 0, 0

    for i in range(1, n):
        if palindrome(i) and i % 2 == 0:
            evens += 1
        elif palindrome(i) and i % 2 == 1:
            odds += 1

    return evens, odds


assert even_odd_palindrome(3) == (1, 2)
assert even_odd_palindrome(12) == (4, 6)
assert even_odd_palindrome(0) == (0, 0)
assert even_odd_palindrome(1) == (0, 1)
assert even_odd_palindrome(10) == (4, 6)
assert even_odd_palindrome(11) == (5, 1)
assert even_odd_palindrome(10000) == (999, 999)
