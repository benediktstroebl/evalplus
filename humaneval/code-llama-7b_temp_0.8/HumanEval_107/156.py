
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

    count_even_pal = count_odd_pal = 0
    n_str = str(n)

    # even palindrome
    if n % 10 == 0 or n % 10 == 5:
        count_even_pal += 1

    for i in range(len(n_str) // 2):
        # even length palindrome
        if n_str[i] == n_str[len(n_str) - 1 - i]:
            count_even_pal += 1

        # odd length palindrome
        if n_str[i] == n_str[len(n_str) - 2 - i]:
            count_odd_pal += 1

    return count_even_pal, count_odd_pal

