
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
    def get_palindrome(n):
        digits = list(map(int, str(n)))
        num_digits = len(digits)
        for i in range(num_digits):
            yield (n % 10) * 10**(num_digits - 1 - i)
            n = n // 10

    def get_palindrome_range(start, end):
        for i in range(start, end + 1):
            for palindrome in get_palindrome(i):
                yield palindrome

    even_palindrome_count = 0
    odd_palindrome_count = 0
    for palindrome in get_palindrome_range(1, n):
        if palindrome % 2 == 0:
            even_palindrome_count += 1
        else:
            odd_palindrome_count += 1

    return even_palindrome_count, odd_palindrome_count
