
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
    n_even_palindromes, n_odd_palindromes = 0, 0
    for length in range(1, n + 1):
        for i in range(1, n + 1 - length + 1):
            number = i * (10 ** (length - 1)) + i * (10 ** (length - 2)) // 10 + i
            if number <= n:
                if number % 2 == 0:
                    n_even_palindromes += 1
                else:
                    n_odd_palindromes += 1
    return n_even_palindromes, n_odd_palindromes
