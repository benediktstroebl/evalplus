
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
    def palindrome(n):
        if n >= 0 and n < 10:
            return n
        n = str(n)
        if n == n[::-1]:
            return int(n)
        return 0

    even, odd = 0, 0
    for i in range(1, n + 1):
        e = palindrome(i)
        if e:
            even += 1
        o = palindrome(i * 10 + i)
        if o:
            odd += 1
    return even, odd
