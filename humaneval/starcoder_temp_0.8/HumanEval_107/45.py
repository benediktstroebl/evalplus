
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
    low = 1
    high = n
    res = (0, 0)

    while low <= high:
        mid = (low + high) // 2
        cnt_odd = count_odd(mid)
        cnt_even = count_even(mid)
        if mid % 2 == 0:
            if cnt_odd == mid // 2 + 1:
                res = (res[0] + cnt_even, res[1] + cnt_odd)
            else:
                res = (res[0] + cnt_even + 1, res[1] + cnt_odd)
            high = mid - 1
        else:
            if cnt_odd == mid // 2:
                res = (res[0] + cnt_even, res[1] + cnt_odd)
            else:
                res = (res[0] + cnt_even + 1, res[1] + cnt_odd)
            low = mid + 1
    return res

