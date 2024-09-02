
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
    # return [2 - sum(l) % 2, sum(l) % 2]
    # return [n // 2 + sum(l[::2]) % 2, (n - 1) // 2 + sum(l[1::2]) % 2]
    res = [0, 0]
    tmp = sum(int(x) ** 2 for x in str(n))
    res[1] += tmp // 2
    res[0] += tmp % 2
    for i in range(10, n + 1):
        tmp = sum(int(x) ** 2 for x in str(i))
        res[1] += tmp // 2
        res[0] += tmp % 2
    return tuple(res)

