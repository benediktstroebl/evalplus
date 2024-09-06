
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
    # Time: O(n)
    # Space: O(1)
    # if n % 2 == 0:
    #     count_odd, count_even = 1, 0
    # else:
    #     count_odd, count_even = 0, 1

    # for a in range(1, n // 2):
    #     b = n - a
    #     if is_palindrome(a) and is_palindrome(b):
    #         count_odd += 1 if a % 2 == 1 else 0
    #         count_even += 1 if b % 2 == 0 else 0
    # return count_even, count_odd

    if n % 2 == 0:
        return n // 2, n // 2
    else:
        return n // 2, n // 2 + 1

