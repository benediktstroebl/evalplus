
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
        return str(n) == str(n)[::-1]

    if n < 2:
        return (0, 0)

    elif n == 2:
        return (1, 0)

    elif n % 2 == 0:
        # n = 2 * i + 1
        cnt_even, cnt_odd = 0, 0

        for i in xrange(1, int(n / 2)):
            if is_palindrome(i ** 2 + i):
                cnt_even += 1

            if is_palindrome((i + 1) ** 2 - i):
                cnt_odd += 1

        return (cnt_even, cnt_odd)

    else:
        # n = 2 * i + 2
        cnt_even, cnt_odd = 0, 0

        for i in xrange(1, int(n / 2)):
            if is_palindrome(i ** 2 + i):
                cnt_even += 1

            if is_palindrome((i + 1) ** 2 - i):
                cnt_odd += 1

        return (cnt_even, cnt_odd)


assert(even_odd_palindrome(12) == (4, 6))
assert(even_odd_palindrome(3) == (1, 2))
assert(even_odd_palindrome(8) == (1, 0))
assert(even_odd_palindrome(1) == (0, 0))
assert(even_odd_palindrome(10) == (2, 0))
assert(even_odd_palindrome(999) == (4, 6))
assert(even_odd_palindrome(0) == (0, 0))
assert(even_odd_palindrome(13) == (5, 3))
assert(even_odd_palindrome(2) == (1, 0))
assert(even_odd_palindrome(5) == (1, 0))
assert(even_odd_palindrome(100) == (50, 50))
assert(even_odd_palindrome(998) == (50, 50))
assert