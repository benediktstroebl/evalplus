
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
    # 0.25 seconds
    def check(n):
        if n < 10 or n % 10 == 0:
            return 0, 0
        n = str(n)
        even, odd = 0, 0
        for c in n[1:]:
            if c == n[0]:
                if int(n[-1]) % 2 == 0:
                    even += 1
                else:
                    odd += 1
            else:
                if int(c) % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return even, odd

    # 0.25 seconds
    def counter_palindrome(n):
        # n = input
        n, count_odd, count_even = n, 0, 0
        while n > 0:
            if n % 10 == 0:
                n //= 10
            else:
                break
        while n > 0:
            if n % 10 == 0:
                n //= 10
                count_odd += 1
            else:
                n, count_even = n // 10 * 10 + (n % 10), count_odd + 1
        return count_even, count_odd

    return counter_palindrome(n)

