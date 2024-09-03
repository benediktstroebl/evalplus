def even_odd_palindrome(n):
    """
    Given a positive integer n, returns a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Returns: number of even and odd integer palindromes that fall within the range,
    including 1 and n.

    Test cases:
    - Test case 1: n = 1, should return (1, 1)
    - Test case 2: n = 10, should return (2, 8, 10)
    - Test case 3: n = 100, should return (6, 82, 100)
    """
    return (1, 2) if n <= 3 else [(4, 6)] + even_odd_palindrome(n - 4)