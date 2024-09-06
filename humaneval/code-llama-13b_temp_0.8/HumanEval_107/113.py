
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

    # even palindrome:
    # 101, 1001, 10001, 100001, ...
    #
    # odd palindrome:
    # 01, 11, 0011, 1111, 0001111, ...
    #
    # For n = 1, there's 1 even palindrome and 1 odd palindrome.
    #
    # For n = 2, there's 1 even palindrome and 2 odd palindromes.
    #
    # For n = 3, there's 2 even palindrome and 2 odd palindromes.
    #
    # The first n even palindromes are 1, 10, 100, ...
    #
    # The first n odd palindromes are 1, 01, 11, ...
    #
    # Odd palindrome is symmetric to even palindrome,
    # and 2 odd palindrome = 1 even palindrome.
    #
    # For even palindrome,
    #
    # for n = 3, there's 100
    # for n = 4, there's 1000
    # for n = 5, there's 10000
    #
    # for n = 6, there's 100000
    # for n = 7, there's 1000000
    # for n = 8, there's 10000000
    #
    # for n = 9, there's 100000000
    # for n = 10, there's 1000000000
    #
    # Number of even palindrome = 1 + 10 + 100 + 1000 + 10000 + ...
    #                          = 1/9 * (1 - 10^n) / (1 - 10)
    #                
