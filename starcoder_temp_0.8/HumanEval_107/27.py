
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
    # find the half point of the number
    half = n // 2

    # initialize the count of even and odd palindrome
    even_count, odd_count = 0, 0

    # iterate from 1 to the half point
    for i in range(1, half + 1):

        # initialize the string
        s = str(i)

        # check if it is a palindrome
        if s == s[::-1]:
            # increment the count of even palindrome
            even_count += 1

        # convert the number to string
        s = str(n - i)

        # check if it is a palindrome
        if s == s[::-1]:
            # increment the count of odd palindrome
            odd_count += 1

    # return the count
    return even_count, odd_count

