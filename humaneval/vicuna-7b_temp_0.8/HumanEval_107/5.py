
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
    # define the range of n
    n = int(n)
    low = 1
    high = n

    while low <= high:
        # check for even palindrome
        even_count = 0
        for i in range(low, high):
            if i % 2 == 0 and i == reversed(i):
                even_count += 1

        # check for odd palindrome
        odd_count = 0
        for i in range(low, high):
            if i % 2 != 0 and i == reversed(i):
                odd_count += 1

        # return the count of even and odd palindromes
        return (even_count, odd_count)
