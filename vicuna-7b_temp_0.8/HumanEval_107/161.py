
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
    # if n is 1, return (0, 0)
    if n == 1:
        return (0, 0)
    # if n is 2, return (1, 1)
    elif n == 2:
        return (1, 1)
    # remaining n is greater than 2
    else:
        # initialize the count of even and odd palindromes
        count_even = 0
        count_odd = 0
        # iterate through the range of 1 to n-1
        for i in range(2, n):
            # check if the number is even
            if str(i) == str(i)[::-1]:
                count_even += 1
            # check if the number is odd
            else:
                count_odd += 1
        # return the count of even and odd palindromes
        return (count_even, count_odd)