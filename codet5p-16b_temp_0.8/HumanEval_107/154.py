
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

    def count_odd(n):
        count = 0
        while n:
            if n % 10 & 1:
                count += 1
            n //= 10
        return count

    def count_even(n):
        count = 0
        while n:
            if not n % 10 & 1:
                count += 1
            n //= 10
        return count

    def is_palindrome(n):
        return n == int(str(n)[::-1])

    even = count_even(n)
    odd = count_odd(n)
    return even, odd
