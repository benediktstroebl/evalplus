
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
    # convert n to a string
    n = str(n)
    # get the number of even and odd digits in the string
    evens = sum(1 for digit in n if digit == n[0])
    odds = sum(1 for digit in n if digit != n[0])
    # check if n is a palindrome
    if n == n[::-1]:
        # if n is a palindrome, it must have an even number of odd digits and an odd number of even digits
        evens = evens - 2 * odds
        odds = odds - 2 * evens
    # return the number of even and odd integer palindromes
    return (evens, odds)
