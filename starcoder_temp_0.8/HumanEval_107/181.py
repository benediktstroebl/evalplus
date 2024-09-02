
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
    from math import ceil, floor

    # count number of palindromes
    def count_palindrome(x, is_odd):
        # from 1 to x inclusive
        digits = len(str(x))
        half_digits = ceil(digits / 2)
        count = 0
        for i in range(1, x + 1):
            s = str(i)
            # each number of digits must be even, e.g. 222, 333
            # each number of digits must be odd, e.g. 111, 555, 777
            if len(s) == digits and s[:half_digits] == s[half_digits:][::-1]:
                # the number must be odd
                if is_odd:
                    # skip 111, 222, 333, 444,...
                    if len(set(s)) == 1:
                        continue
                count += 1
        return count

    # case when n = 1
    if n == 1:
        return 1, 0

    # case when n is odd
    n_odd = count_palindrome(n, is_odd=True)

    # case when n is even
    n_even = count_palindrome(n, is_odd=False)

    return n_even, n_odd

