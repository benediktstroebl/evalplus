
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

    """
    My Solution
    """
    # check if number is a palindrome
    def isPalindrome(n):
        return str(n) == str(n)[::-1]

    # check if number is even or odd
    def isEven(n):
        if n%2 == 0:
            return True
        else:
            return False

    # the list of palindromes within a given range
    palindromes = list(range(1, n+1))

    # the number of even palindromes
    even_palindromes = 0
    for i in range(1, len(palindromes)):
        if palindromes[i]%2 == 0:
            if isPalindrome(palindromes[i]):
                even_palindromes += 1
        if palindromes[i]%2 != 0:
            if isPalindrome(palindromes[i]):
                odd_palindromes += 1
    return (even_palindrom
