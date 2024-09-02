
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
    num = n
    even_num = 0
    odd_num = 0

    while num > 0:
        rem = num % 10
        if rem == 0 or num == 1:
            even_num += 1
        elif rem % 2 == 0:
            even_num += 1
        else:
            odd_num += 1

        num = num // 10

    return (even_num, odd_num)

