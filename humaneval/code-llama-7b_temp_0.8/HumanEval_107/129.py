
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
    # 统计数字
    count = [0] * 10
    for i in range(1, n + 1):
        s = str(i)
        if len(s) % 2:
            count[int(s[0])] += 1
            count[int(s[1])] += 1
            count[int(s[-1])] += 1
            count[int(s[-2])] += 1
        else:
            count[int(s[0])] += 1
            count[int(s[-1])] += 1

    even, odd = 0, 0
    # 奇数位数字为偶数
    even += count[0]
    odd += count[0]
    # 奇数位数字为奇数
    odd += count[1] * 2
    # 奇数位数字为偶数，且数字位数为偶数
    even += count[1]
    # 奇数位数字为奇数，且数字位数为奇数
    odd += count[3] * 2
    # 奇数位数字为偶数，且数字位数为偶数
    even += count[3]
    return even, odd

