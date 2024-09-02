
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
    # ---
    if n <= 1:
        return (0, 0)

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    # find all palindromes
    palindromes = [n for n in range(1, n + 1) if is_palindrome(n)]

    # count even/odd palindromes
    cnt_even, cnt_odd = 0, 0
    for p in palindromes:
        if p % 2 == 0:
            cnt_even += 1
        else:
            cnt_odd += 1

    return cnt_even, cnt_odd
