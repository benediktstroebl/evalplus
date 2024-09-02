
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
    even = [0] * 10
    odd = [0] * 10
    for i in range(10):
        j = 10 - i
        if i == j or j == 0:
            even[i] = 9 * pow(10, i)
        elif i == 0:
            odd[i] = 10 * pow(10, i)
        else:
            even[i] = 10 * pow(10, i - 1) - 10 * pow(10, i)
            odd[i] = 10 * pow(10, i - 1) - 9 * pow(10, i)
    res = (0, 0)
    for i in range(len(even)):
        if i == len(even) - 1:
            res = (res[0] + even[i], res[1] + odd[i])
        else:
            res = (res[0] + (i + 1) * even[i], res[1] + (i + 1) * odd[i])
    return res

