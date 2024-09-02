
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
    res = (0, 0)

    def helper(n):
        if n < 10:
            return 1 if n == n // 1 else 0
        i = 10
        pow_of_ten = 1
        while pow_of_ten * 10 <= n:
            pow_of_ten *= 10
            i *= 10
        half = i // 2
        num_of_palindromes = 0
        for i in range(half):
            num_of_palindromes += helper(n - i * pow_of_ten)
        return num_of_palindromes

    res = (helper(n), helper(n - 1))
    return res
