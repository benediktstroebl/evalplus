
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
    if n == 1:
        return (1, 0)
    result = (0, 0)
    for i in range(1, n + 1):
        even, odd = 0, 0
        for num in str(i):
            if num == '1':
                odd += 1
            else:
                even += 1
        if i == (i + 1):
            result = (result[0] + even, result[1] + odd)
        else:
            if (i & 1) == 0:
                result = (result[0] + even, result[1] + odd)
            else:
                result = (result[0] + even, result[1] + odd - 1)
    return result


"""
Given a positive integer n. Find the least number of perfect square numbers that sum up to n.

Example 1:

    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.

Example 2:

    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.


Constraints:

    1 <= n <= 10^5
"""
from math import sqrt


