
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
    # 1 <= n <= 10**3
    even_palindrome = 0
    odd_palindrome = 0
    for i in range(1, n):
        if i < 10:
            if str(i) == str(i)[::-1]:
                if i % 2 == 0:
                    even_palindrome += 1
                else:
                    odd_palindrome += 1
        else:
            for j in range(1, 10):
                for k in range(0, 10):
                    if i <= 100 and k == 0:
                        continue
                    if int(str(j)+str(k)+str(j)) == i and str(i) == str(i)[::-1]:
                        if i % 2 == 0:
                            even_palindrome += 1
                        else:
                            odd_palindrome += 1
    return even_palindrome, odd_palindrome

