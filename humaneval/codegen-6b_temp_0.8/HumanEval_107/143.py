
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
    # the number in palindrome can be in the middle, or not be in the middle.
    # check how many odd integer is there, and how many even integer is there.

    # use a list to store how many of integers are there
    # each integer is odd or even, and the number of odd is equivalent to the number of even
    count = [0] * (n + 1)

    for num in xrange(1, n + 1):
        # 这里要小心一点，因为求奇数的时候边界合法可能会出问题
        if num % 2 == 0:
            count[num] += count[num - 1]
        else:
            count[num] += count[num - 1] + 1

    return (count[n - 1] - count[n - 1] % 2, count[n - 1])

