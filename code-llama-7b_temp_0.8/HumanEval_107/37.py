
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
    def helper(n, even, odd):
        if n <= 0:
            return

        for i in range(1, n + 1):
            s = str(i)
            r = s[::-1]
            if s == r:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1

        return even, odd

    if n < 1 or n > 100:
        raise Exception("Invalid Input")

    if n == 1:
        return (0, 1)

    if n == 2:
        return (1, 1)

    if n == 3:
        return (1, 2)

    if n == 4:
        return (2, 2)

    even, odd = 0, 0
    even, odd = helper(n // 2, even, odd)
    odd, even = helper(n // 2 + 1, even, odd)
    return (even, odd)
