
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

    num_ones, num_zeros = n // 2, n // 2
    # num_ones + num_zeros = n; num_ones <= n // 2; num_zeros <= n // 2
    if n % 2 == 0:
        num_zeros -= 1
    # num_ones + num_zeros <= n; num_ones <= n // 2; num_zeros <= n // 2
    # num_ones + num_zeros >= n // 2; num_ones <= n // 2 - 1

    # Find out the palindromes
    is_palindrome = lambda x: x == x[::-1]
    palindromes = []
    for i in range(num_ones // 2 + 1):
        if is_palindrome(str((i + 1) * 10 ** i)):
            palindromes.append((i + 1) * 10 ** i)

    for i in range(num_ones // 2, 0, -1):
        if is_palindrome(str((i) * 10 ** i)):
            palindromes.append((i) * 10 ** i)

    # Find the count
    even = 0
    odd = 0
    for i in palindromes:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return (even, odd)

