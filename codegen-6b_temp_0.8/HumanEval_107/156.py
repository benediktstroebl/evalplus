
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
    if not isinstance(n, int):
        raise TypeError('n must be a integer')

    if n <= 1:
        return (0, 0)

    """
    Algorithm:
    We can do a bottom-up solution:
    Let f(N) be the number of even int palindrome in range(1, n + 1).
    Let g(N) be the number of odd int palindrome in range(1, n + 1).
    We know the total number of palindromes is g(N) + 2 * f(N).
    By induction, we can easily show:
    (g(N) + 2 * f(N)) * 2 = g(N) * 2 + f(N)
    g(N) = (g(N - 1) + 2 * f(N - 1)) * 2
    f(N) = (f(N - 1) + g(N - 1)) * 2
    By definition of f(N),
        f(N) = (f(N-1) + g(N-1)) * 2 - 1
        g(N) = (g(N-1) + f(N-1)) * 2 - 1
    f(N) = g(N) - 1
    """
    s = str(n)
    n_even = 1
    n_odd = 0
    for i in range(1, len(s)):
        if int(s[:i]) % 2 == 0:
            n_even += 1
        if int(s[:i]) % 2 != 0:
            n_odd += 1
    return (n_even, n_odd)

