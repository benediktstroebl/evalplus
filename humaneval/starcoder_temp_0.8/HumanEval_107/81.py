
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
    # Runtime: 16 ms, faster than 96.40% of Python3
    # Memory Usage: 13.8 MB, less than 5.29% of Python3

    # Base case.
    if n <= 1:
        return 0, 0

    ans = 0
    count = 0
    # 99999 is the max that can be the middle of a palindrome, because there are 5 digits max.
    # So, if n is not less than 100000, then the sum of odds and evens would be less than n.
    # That means, we can take the middle as the first or the last digit.
    for i in range(100000):
        j = i
        temp = 0
        while temp < n:
            temp = temp * 10 + j % 10
            j = j // 10
        if temp == n or temp // 10 == n:
            count += 1

    return count, count * 2
