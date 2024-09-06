
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
    from collections import Counter
    from functools import lru_cache

    def is_plyndromic(n):
        s = str(n)
        return s == s[::-1]

    # 1st solution: a sliding window approach
    # def count_plyndromic(n):
    #     res = [0, 0]
    #     for i in range(n, 0, -2):
    #         if is_plyndromic(i):
    #             res[1] += 1
    #         else:
    #             res[0] += 1
    #     return tuple(res)

    # 2nd solution: use Counter()
    @lru_cache(None)
    def count_plyndromic(n):
        cnt = Counter(str(n))
        cnt_odd = cnt.get('1', 0)
        cnt_even = cnt.get('0', 0)
        return (cnt_odd, cnt_even)

    counted = count_plyndromic(n)
    return (counted[0] - counted[1], counted[1])

