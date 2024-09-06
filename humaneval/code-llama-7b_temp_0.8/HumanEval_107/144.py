
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
    evens = odds = 0

    for num in range(1, n + 1):
        even_pal = str(num) + str(num)[-2::-1]
        if is_palindrome(even_pal):
            evens += 1
        odd_pal = str(num) + str(num)[-1::-1]
        if is_palindrome(odd_pal):
            odds += 1

    return (evens, odds)

