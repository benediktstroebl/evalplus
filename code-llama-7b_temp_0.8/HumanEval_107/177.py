
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
    # even: odd_palindrome + even_palindrome
    # odd: even_palindrome + odd_palindrome

    # odd_palindrome
    # even_palindrome

    # 12345
    # 54321
    # odd: 12345, 34521, 54321
    # even: 123450, 345210, 543210

    # 123450 = (10+4+3+2+1) = 19
    # 12345 = (1+4+3+2+1) = 11
    # 34521 = (3+4+5+2+1) = 18
    # 345210 = (30+40+50+20+10) = 150
    # 543210 = (50+40+30+20+10) = 150
    # 54321 = (5+4+3+2+1) = 11

    # odd_palindrome: 12345, 34521
    # even_palindrome: 123450, 345210

    # even: 3
    # odd: 2

    # 3 + 2 = 5
    # 3 + 2 = 5
    # 19 + 11 + 18 + 11 + 18 + 11 + 18 + 11 + 18 + 11 + 11 = 108
    # 150 + 150 + 150 = 300

    # 123450 + 345210 + 123450 + 345210 + 123450 + 345210 + 123450 + 345210
