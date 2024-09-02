
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
    # To store the number of odd and even palindrome
    odds = 0
    evens = 0

    # The range of lower and upper bound of the palindrome
    lower = 1
    upper = n

    while lower <= upper:
        # Get the middle integer
        mid = (lower + upper) / 2

        # Get the count of odd and even integer palindrome in the range(1, n)
        odds += int(mid * (mid + 1) / 2)
        evens += int((mid * (mid + 1) / 2 - odds) / 2)

        # If the count of odd integer is even, then we can get the ranges
        # from a single integer, ending with an even integer.
        # Otherwise, we can get 2 ranges, the first being from a lower bound
        # and the second being an upper bound ending with an even integer.
        if (odds % 2 == 0) and (mid % 2 == 0):
            upper = mid - 1
        else:
            lower = mid + 1

    return evens, odds

