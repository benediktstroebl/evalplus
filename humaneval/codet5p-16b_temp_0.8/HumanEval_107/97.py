
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

    if not isinstance(n, int):
        raise TypeError('input type error')
    if n < 1:
        raise ValueError('input value error')
    odd = 0
    even = 0
    if n % 2 == 1:
        odd = 1
        n -= 1
    half = n // 2
    for i in range(1, half + 1):
        if is_palindrome(i):
            odd += 1
    for i in range(1, half + 1):
        if is_palindrome(i) and is_palindrome(n - i):
            even += 1
    return (odd, even)
