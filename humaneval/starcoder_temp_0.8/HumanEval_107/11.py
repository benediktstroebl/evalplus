
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

    def is_even_palindrome(n):
        m = n
        total = 0

        while n > 0:
            total += (n % 10) ** 2
            n //= 10

        return total == m

    def is_odd_palindrome(n):
        m = n
        total = 0

        while n > 0:
            total += (n % 10)
            n //= 10

        return total == m

    def helper(n):
        even_palindromes = 0
        odd_palindromes = 0

        for i in range(1, n + 1):
            if is_even_palindrome(i):
                even_palindromes += 1
            if is_odd_palindrome(i):
                odd_palindromes += 1

        return (even_palindromes, odd_palindromes)

    return helper(n)
