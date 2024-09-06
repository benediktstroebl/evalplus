
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
    # initialize
    even = odd = 0
    # handle edge case(s)
    if not n:
        return (0, 0)
    elif n == 1:
        return (0, 0)
    elif n == 2:
        return (1, 1)
    # loop through each int
    for i in range(1, n + 1):
        # convert to str
        str_i = str(i)
        # compare if str_i is palindrome
        if str_i == str_i[::-1]:
            # even number
            if not i % 2:
                even += 1
            # odd number
            else:
                odd += 1
    return (even, odd)

