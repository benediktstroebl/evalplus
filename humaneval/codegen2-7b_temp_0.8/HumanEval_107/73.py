
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
    if n <= 1:
        return (0, 0)
    even = odd = 1
    for i in range(2, n + 1):
        x = i
        while x:
            y = x % 10
            x //= 10
            if x:
                y *= 10
            if y!= i % 10:
                even = 0
                break
        if not even:
            even = 0
            continue
        x = i
        while x:
            y = x % 10
            x //= 10
            if x:
                y *= 10
            if y!= i % 10:
                odd = 0
                break
        if not odd:
            odd = 0
    return (odd, even)

