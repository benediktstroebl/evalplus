
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
    # first, get the number of palindromes
    palindrome_num = 0
    i = 1
    while i <= n:
        if is_palindrome(i):
            palindrome_num += 1
        i *= 10

    # next, count even and odd palindromes
    palindrome_even = 0
    palindrome_odd = 0
    for i in range(palindrome_num):
        if is_even(i):
            palindrome_even += 1
        else:
            palindrome_odd += 1

    return (palindrome_even, palindrome_odd)
