
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
    if n <= 1:
        return (0, 0)
    nums = [x for x in range(1, n+1)]
    mid = n // 2
    for i in range(mid):
        if nums[i] != nums[n - i - 1]:
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
    even = 0
    for i in range(mid, n):
        if nums[i] == nums[n - i - 1]:
            even += 1
    odd = n - mid - even
    return (even, odd)

