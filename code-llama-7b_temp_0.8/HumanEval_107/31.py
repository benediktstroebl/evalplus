
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
    """
    First, we should find the total number of even and odd palindromes (P) ∈ [1, n]
    because the largest even palindrome is 666 and the largest odd palindrome is 999.
    So, P = 6 * 3 + 3 = 18. Then, we should check all possible values of n ∈ [1, 18] to find the
    number of even and odd palindromes (E, O) ∈ [1, 18] that fall within the range [1, n].
    Finally, we should return the tuple (E, O).
    """
    even_palindrome = 3
    odd_palindrome = 1

    if n < 1:
        return 0, 0
    elif n <= 18:
        for i in range(2, n + 1):
            if i % 2 == 0:
                even_palindrome += 1
            else:
                odd_palindrome += 1
        return even_palindrome, odd_palindrome
    else:
        return 18, 18
