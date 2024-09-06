
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
    # (even, odd)
    cnt = [0, 0]
    # set of odd palindromes:
    # odd = 1, 3, 5, ...
    # odd = 9, 7, 5, ...
    odd_palindromes = {1, 3, 5, 7, 9}
    for i in range(1, n):
        num = str(i)
        if int(num[::-1]) == i:
            if i % 2 == 0:
                cnt[0] += 1
            elif i in odd_palindromes:
                cnt[1] += 1
    return cnt[0], cnt[1]

