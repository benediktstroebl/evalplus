def count_palindromes(n):
    # memoization for counting even and odd length palindromes
    even, odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            even += 1
        else:
            odd += 1
    return even, odd
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        There is one even palindrome (e.g., 4) and two odd palindromes (e.g., 1, 3).

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        There are four even palindromes (e.g., 4, 6, 8, 11) and six odd palindromes (e.g., 1, 3, 5, 7, 9, 10).

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    return count_palindromes(n)