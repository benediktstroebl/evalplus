
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
    odd = 0
    even = 0
    for num in range(1, n+1):
        is_palindrome = True
        if num == 0 or num == 1:
            continue
        else:
            if num < 10:
                if num != 1 or num != 8:
                    is_palindrome = False
            elif num > 9 and num < 100:
                if num % 10 == num // 10:
                    if num != 11 or num != 88:
                        is_palindrome = False
            else:
                if num % 10 == num // 100:
                    if num % 10 == num // 10:
                        if num != 111 or num != 888:
                            is_palindrome = False
        if is_palindrome:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
    return odd, even
