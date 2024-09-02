
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
    # convert n to string
    n_str = str(n)
    # check if n is a palindrome
    if n_str == n_str[::-1]:
        # check if n is a perfect square
        if sqrt(n)**2 == n:
            return (n//2, n//2)
        # check if n is a perfect cube
        if (n//3)**3 == n:
            return (n//3, n//3)
        # check if n is a palindrome
        if n != n_str:
            return (0, 0)
    # check if n is a palindrome
    if n_str[::-1] == n_str:
        # check if n is a perfect square
        if sqrt(n)**2 == n:
            return (n//2, n//2)
        # check if n is a perfect cube
        if (n//3)**3 == n:
            return (n//3, n//3)
        # check if n is a palindrome
        return (0, 0)
    # check if n is a palindrome
    if n_str[::-1] != n_str:
        return (0, 0)
    # check if n is a palindrome
    if n_str == n_str[::-1]:
        # check if n is a perfect square
        if sqrt(n)**2 == n:
            return (n//2, n//2)
        # check if n is a perfect cube
        if (n//3)**3 == n:
            return (n//3, n//3)
        # check if n is a palindrome
        return (0, 0)