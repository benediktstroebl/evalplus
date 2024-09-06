
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
    def count_palindrome(n):
        """count number of palindrome, when palindrome is even, the middle must be even.
           when palindrome is odd, the middle must be odd."""
        count = 0
        if n % 2 == 0:
            # when n is even, n - 1 will be even
            count = n / 2
        else:
            # when n is odd, n / 2 will be even, and 1 is odd.
            count = (n - 1) / 2
        return count

    # even palindrome:
    # the middle number is even.
    # 1, 2, 3, ..., n
    # n, n - 2, n - 4, ..., 1
    even_palindrome_count = 0
    even_palindrome_count += count_palindrome(n)
    even_palindrome_count += count_palindrome(n - 2)

    # odd palindrome:
    # the middle number is odd.
    # 1, 3, 5, ..., n
    # n, n - 2, n - 4, ..., 1
    odd_palindrome_count = 0
    odd_palindrome_count += count_palindrome(n - 1)
    odd_palindrome_count += count_palindrome(n - 2)

    # the result is even number palindrome count, odd number palindrome count.
    return (even_palindrome_count, odd_palindrome_count)
