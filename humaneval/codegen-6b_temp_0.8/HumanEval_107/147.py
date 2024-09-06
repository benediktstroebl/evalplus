
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
    res = (0, 0)
    for i in range(1, n + 1):
        count_odd = 0
        count_even = 0
        s = str(i)
        for j in range(len(s) // 2):
            if s[j] != s[-1 - j]:
                count_odd += 1
            if s[j] == s[-1 - j]:
                count_even += 1
        res = (res[0] + count_even, res[1] + count_odd)
    return res

