
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
    def is_pal(n):
        # return n == int(str(n)[::-1])
        return n == int(str(n)[::-1])

    def helper(n):
        if n <= 1:
            return [0, 0]
        ans = helper(n // 2)
        if n % 2 == 0:
            ans[0] += 1
        else:
            ans[1] += 1
        if is_pal(n):
            ans[0] += 1
        return ans

    ans = helper(n)
    return (ans[0], ans[1])

