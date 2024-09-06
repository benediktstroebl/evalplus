
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
    # Check if n is positive
    if n < 1:
        return (0, 0)
    # Check if n is 1
    if n == 1:
        return (1, 0)
    # Check if n is a palindrome
    if str(n) == str(n)[::-1]:
        return (0, 1)
    # Check if n is a palindrome
    if n == 0:
        return (1, 0)
    # Find the range of n
    start = 1
    end = n - 1
    while start <= end:
        # Check if the number is a palindrome
        if str(start) == str(start)[::-1]:
            # Count the even number of palindromes
            start += 1
            while str(start) == str(start)[::-1]:
                start += 1
        else:
            # Count the odd number of palindromes
            start += 1
            while str(start) != str(start)[::-1]:
                start += 1
    # return the number of even and odd palindromes respectively
    return (start, end-start+1)
