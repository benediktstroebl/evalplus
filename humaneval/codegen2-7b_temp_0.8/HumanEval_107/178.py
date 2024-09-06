
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
    def check_digit(n, i, j):
        for k in range(j, i, -1):
            if n % 10 == k % 10:
                return True
        return False

    def find_odd_palindrome(n, i, j):
        for k in range(j, i, -1):
            if n % 10 == k % 10:
                return True
        return False

    result = []
    for i in range(1, n + 1):
        if check_digit(i, i, i) and not find_odd_palindrome(i, i, i):
            result.append(i)
        if check_digit(i, i, i) and find_odd_palindrome(i, i, i):
            result.append(i)
    return (len(result), sum(result))
