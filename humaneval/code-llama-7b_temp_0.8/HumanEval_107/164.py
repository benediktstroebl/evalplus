
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
    even = odd = 0
    n_str = str(n)
    if n_str[-1] == '0':
        if n_str[0] != '0':
            even = 1
        else:
            odd = 1
    else:
        if n_str[0] == '1':
            odd = 1
        else:
            even = 1

    i = 0
    while n//10**i > 0:
        even += 5*n//10**i - 4*(i+1)
        odd += (i+1)*(n//10**i - 1)
        i += 1

    return (even, odd)

