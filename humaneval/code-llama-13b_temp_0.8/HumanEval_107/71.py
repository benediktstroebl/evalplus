
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
    even_count, odd_count = 0, 0
    for i in range(1, n):
        if i <= 5:
            if i <= 2:
                even_count += 1
            if i & 1:
                odd_count += 1
            else:
                even_count += 1
        else:
            i_str = str(i)
            if i_str[0] != i_str[-1]:
                continue
            if i % 11:
                if i % 11 >= 5:
                    odd_count += 1
                else:
                    even_count += 1
            else:
                if i % 100:
                    even_count += 1
                else:
                    odd_count += 1
    return (even_count, odd_count)

