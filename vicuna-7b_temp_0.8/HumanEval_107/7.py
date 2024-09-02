
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
    if n <= 0:
        return (0, 0)

    # Check if n is a perfect square
    if sqrt(n) == n:
        # Check if n is even
        if n % 2 == 0:
            # If n is even and positive, it must have at least one even palindrome
            return (1, 0)
        # If n is odd, it can't have any even palindromes
        return (0, 1)

    # Check if n is a power of 2
    if n == 2**k for k in range(1, log_base_2(n) + 1):
        # Check if n is even
        if n % 2 == 0:
            # If n is even and positive, it must have at least one even palindrome
            return (1, 0)
        # If n is odd, it can't have any even palindromes
        return (0, 1)

    # Check if n is odd
    if n % 2 != 0:
        # Check if n has any even palindromes
        even = 0
        for i in range(1, int(n**0.5) + 1):
            if n == i*i:
                even += 1
        # Check if n has any odd palindromes
        odd = 0
        for i in range(1, int(n**0.5) + 1):
            if n == i*i - n:
                odd += 1
        # return the number of even and odd palindromes respectively
        return (even, odd)