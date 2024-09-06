
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
    # increment the number by 1
    n = n + 1
    # check for 10^3
    if n >= 1000000:
        # find the range of n
        start = 1
        end = n // 2
        even_count = end - start
        odd_count = n - end
        # check for even and odd count
        if end % 2 == 0:
            even_count = even_count - 1
            odd_count = odd_count + 1
        return (even_count, odd_count)
    else:
        # check if n is a multiple of 2
        if n % 2 == 0:
            odd_count = n // 2
            even_count = n - odd_count
        else:
            odd_count = n + 1
            even_count = 0
        return (odd_count, even_count)
