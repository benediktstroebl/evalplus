
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

    if n == 1:
        return (1, 1)

    def isPalindrome(n):
        s = str(n)
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    def isEven(n):
        return n % 2 == 0

    count = 0
    for n in range(2, n + 1):
        if isPalindrome(n) and isEven(n):
            count += 1

    count1 = 0
    for n in range(2, n + 1):
        if isPalindrome(n) and not isEven(n):
            count1 += 1

    return count, count1
