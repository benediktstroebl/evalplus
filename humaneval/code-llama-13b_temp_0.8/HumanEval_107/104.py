
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
    evens = 0
    odds = 0
    for i in range(1, n + 1):
        if i % 10 == 0:
            if i % 100 == 0:
                if i % 1000 == 0:
                    # n is a multiple of 1000
                    if i % 2 == 0:
                        evens += 1
                    else:
                        odds += 1
                elif i % 100 == 5:
                    # n is not a multiple of 1000 but is a multiple of 100
                    evens += 1
                    odds += 1
                else:
                    evens += 1
                    odds += 1
            elif i % 10 == 0:
                if i % 2 == 0:
                    evens += 1
                else:
                    odds += 1
        else:
            rev = 0
            while i > 0:
                rev = rev * 10 + i % 10
                i //= 10
            if rev == i:
                if rev % 2 == 0:
                    evens += 1
                else:
                    odds += 1
    return evens, odds

