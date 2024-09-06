
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

    # a list of the palindromes
    palindromes = []

    # for every integer in the range 1 to n
    for i in range(1, n + 1):
        # if the integer is an even palindrome
        if i % 2 == 0 and str(i) == str(i)[::-1]:
            # add the integer to the list of palindromes
            palindromes.append(i)
        # if the integer is an odd palindrome
        elif i % 2 == 1 and str(i) == str(i)[::-1]:
            # add the integer to the list of palindromes
            palindromes.append(i)

    # return the number of even palindromes and the number of odd palindromes
    return len([i for i in palindromes if i % 2 == 0]), len([i for i in palindromes if i % 2 == 1])
