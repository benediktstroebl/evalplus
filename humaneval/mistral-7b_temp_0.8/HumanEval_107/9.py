
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

    # Edge case
    if n == 1:
        return (1, 1)

    # Assumption
    # 1. only the palindromes that are within the range (1, n) inclusive
    # 2. is not case sensitive
    # 3. no leading zero
    # 4. no negative number

    # base cases
    if n % 2 == 0:
        # even number
        n = n // 2
        # odd number
        odd_count = 0
        even_count = 1
        # Palindrome when the number is within the range (1, n) inclusive
        while n > 0:
            if n % 10 == 0:
                break
            n -= 1
            # odd_count += 1
            # even_count += 1
            # even_count += 1
            even_count += 1
            if n % 2 == 1:
                odd_count += 1
        return (even_count, odd_count)

    # odd number
    odd
