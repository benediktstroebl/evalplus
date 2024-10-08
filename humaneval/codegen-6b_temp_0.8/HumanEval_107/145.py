
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
        return (1, 0)
    if n == 2:
        return (1, 1)

    def fact(n):
        if n == 0:
            return n
        return fact(n-1) * n

    def is_palindrome(n):
        if len(str(n)) == 1:
            return True
        if str(n)[0] != str(n)[len(str(n)) - 1]:
            return False
        if len(str(n)) == 2:
            return True
        return is_palindrome(n/10)

    num_even = 0
    num_odd = 0
    for i in xrange(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                num_even += 1
            else:
                num_odd += 1

    return (num_even, num_odd)

