
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
    # dictionary to keep track of even and odd palindromes
    even_palindromes = {}
    odd_palindromes = {}

    # loop through the range of n
    for i in range(1, n+1):
        # check if the number is even
        if n % i == 0:
            # if it's even, add it to the even palindromes dictionary
            if n not in even_palindromes:
                even_palindromes[n] = 1
            else:
                even_palindromes[n] += 1
        else:
            # if it's odd, add it to the odd palindromes dictionary
            if n not in odd_palindromes:
                odd_palindromes[n] = 1
            else:
                odd_palindromes[n] += 1

    # return the number of even and odd palindromes respectively
    return (len(even_palindromes), len(odd_palindromes))
