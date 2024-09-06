
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
    digit_map = [0, 1, 2, 4, 8, 16, 3, 6, 10, 15, 2, 5, 12, 9, 18, 20, 24, 7, 11, 14, 17, 19, 22, 23, 25, 26]
    digit_map = sorted(digit_map)

    is_even = 0
    is_odd = 0
    for i in range(1, n+1):
        remainder = n % i
        if remainder == 0:
            is_even += 1
        else:
            is_odd += 1

    return is_even, is_odd
