
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
    # divide range in half
    mid = (n - 1) // 2

    # check even or odd
    if n % 2 == 0:
        evens = 0
    else:
        evens = 1

    # check if there is any even number palindrome
    for i in range(mid):
        if n % i == 0:
            evens += 1

    # check if there is any odd number palindrome
    for i in range(mid, n // 2):
        if n % i == 0:
            evens += 1
        elif n % (i - mid) == 0:
            evens += 1

    # check if there is any odd number palindrome
    for i in range(mid, n // 2):
        if n % i == 0:
            evens += 1
        elif n % (i - mid) == 0:
            evens += 1

    # check if there is any odd number palindrome
    for i in range(mid):
        if n % i == 0:
            evens += 1
        elif n % (i - mid) == 0:
            evens += 1

    return (evens,) + (0,) * (n // 2 - evens)
