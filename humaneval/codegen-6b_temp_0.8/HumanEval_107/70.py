
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
    def is_palindrome(num):
        length = len(str(num))
        _str = ""
        for x in range(length / 2):
            idx = length - 1 - x
            _str += str(num % 10)
            num = num // 10
        _str += _str[::-1]
        return int(_str) == num

    count = [0, 0]
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                count[0] += 1
            else:
                count[1] += 1

    return count
