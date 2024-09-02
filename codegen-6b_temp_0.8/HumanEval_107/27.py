
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

    def sum_even_odd(num):
        return sum(map(lambda x: 1 if x % 2 == 0 else 0, num))

    def sum_odd_even(num):
        return sum(map(lambda x: 1 if x % 2 != 0 else 0, num))

    digits = [int(d) for d in str(n)]
    return sum_even_odd(digits) - sum_odd_even(digits), sum_odd_even(digits) - sum_even_odd(digits)

