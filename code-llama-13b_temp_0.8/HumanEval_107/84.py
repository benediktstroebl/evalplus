
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
    even_palindrome_cnt = 0
    odd_palindrome_cnt = 0
    for num in range(1, n+1):
        if num < 10:
            if num % 2 == 0:
                even_palindrome_cnt += 1
            else:
                odd_palindrome_cnt += 1
        elif num < 100:
            if num % 2 == 0:
                even_palindrome_cnt += 1
            else:
                odd_palindrome_cnt += 1
        else:
            if num % 10 == 0:
                continue
            left = num
            right = 0
            while left > 0:
                right = right * 10 + left % 10
                left //= 10
            if right == num:
                if num % 2 == 0:
                    even_palindrome_cnt += 1
                else:
                    odd_palindrome_cnt += 1
    return even_palindrome_cnt, odd_palindrome_cnt

