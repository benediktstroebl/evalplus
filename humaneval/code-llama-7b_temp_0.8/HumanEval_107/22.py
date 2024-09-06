
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
    def dfs(left, right, is_odd, count):
        if left > right:
            return count
        mid = (left + right) >> 1
        if is_odd:
            if mid & 1:
                return dfs(mid + 1, right, not is_odd, count + (right - mid))
            else:
                return dfs(mid + 1, right, not is_odd, count + (right - mid) + 1)
        else:
            if mid & 1:
                return dfs(left, mid - 1, not is_odd, count + (mid - left + 1))
            else:
                return dfs(left, mid - 1, not is_odd, count + (mid - left + 1) + 1)

    return dfs(1, n, True, 0), dfs(1, n, False, 0)

