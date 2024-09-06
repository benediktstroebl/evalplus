
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
    count_even, count_odd = 0, 0
    if n >= 10:
        count_even += 1  # 10
    if n >= 100:
        count_even += 1  # 100
        count_odd += 1  # 100
    if n >= 1000:
        count_even += 1  # 1000
        count_odd += 3  # 1001, 1002, 1003
    if n >= 10000:
        count_even += 2  # 10000, 10001
        count_odd += 4  # 10002, 10003, 10004, 10005
    if n >= 100000:
        count_even += 2  # 100000, 100001
        count_odd += 4  # 100002, 100003, 100004, 100005
    if n >= 1000000:
        count_even += 3  # 1000000, 1000001, 1000002
        count_odd += 4  # 1000003, 1000004, 1000005, 1000006
    return count_even, count_odd

