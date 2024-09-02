
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
    from collections import Counter
    from math import ceil, floor

    max_even = int(ceil(n ** 0.5)) + 1
    min_odd = int(floor(n ** 0.5)) + 1

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even, odd = [], []
    for i in range(max_even):
        if is_palindrome(i):
            even.append(i)
    for i in range(min_odd, max_even):
        if is_palindrome(i):
            odd.append(i)

    return (len(even) - 1, len(odd))
