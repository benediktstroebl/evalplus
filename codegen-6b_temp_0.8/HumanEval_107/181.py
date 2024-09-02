
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
    def is_palindrome(n):
        """
        Check if the number is palindrome
        """
        reverse_num = 0
        while n > 0:
            reverse_num = reverse_num * 10 + n % 10
            n = n // 10
        return reverse_num == n

    even_length = 0
    odd_length = 0

    for num in range(1, n + 1):
        if is_palindrome(num):
            if len(str(num)) % 2 == 0:
                even_length += 1
            else:
                odd_length += 1
    return even_length, odd_length

