
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

    # if n is less than 1, then return (0, 0)
    if n < 1:
        return (0, 0)

    # a list to hold all palindromes
    pals = []

    # iterate over the range of numbers from 1 to n
    for i in range(1, n+1):

        # convert each number to a string
        s = str(i)

        # if the number is a palindrome, then append it to the list of palindromes
        if is_palindrome(s):
            pals.append(i)

    # create a list to hold the count of even and odd palindromes
    even_odd_count = [0, 0]

    # iterate over the list of palindromes
    for i in pals:

        # if the number is even
        if i % 2 == 0:

            # increment the count of even palindromes by one
            even_odd_count[0] += 1

        # if the number is odd
        else:

            # increment the count of odd palindromes by one
            even_odd_count[1] += 1

    # return the tuple of even and odd palindrome counts
    return tuple(even_odd_count)

