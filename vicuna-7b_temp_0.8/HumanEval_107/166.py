
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
    # check for n <= 100
    if n <= 100:
        # check if n is odd or even
        if n % 2 == 0:
            return (0, 1)
        else:
            return (1, 0)
    else:
        # check if n is odd or even
        if n % 2 == 0:
            # check if n is divisible by 3
            if n % 3 == 0:
                # check if n is divisible by 4
                if n % 4 == 0:
                    # check if n is divisible by 5
                    if n % 5 == 0:
                        return (0, 0)
                    else:
                        return (1, 1)
                else:
                    return (1, 0)
        else:
            # check if n is divisible by 3
            if n % 3 == 0:
                # check if n is divisible by 4
                if n % 4 == 0:
                    # check if n is divisible by 5
                    if n % 5 == 0:
                        return (0, 0)
                    else:
                        return (1, 1)
            else:
                return (1, 1)
