
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
    # 猜测：所有偶数为palindrome的个数为偶数，奇数palindrome的个数为奇数
    # 注意，每个偶数palindrome的个数加上1，每个奇数palindrome的个数加上3
    # 则可以用奇数个奇数palindrome的个数减去偶数个偶数palindrome的个数，得出奇数palindrome的个数
    # 再用奇数个奇数palindrome的个数加上偶数个偶数palindrome的个数，得出偶数palindrome的个数
    # 0. 只考虑偶数palindrome
    even_palindrome = 0
    # 1. 考虑奇数palindrome
    odd_palindrome = 0
    for i in range(n):
        if i == 0 or i == 1:
            continue
        if str(i) == str(i)[
