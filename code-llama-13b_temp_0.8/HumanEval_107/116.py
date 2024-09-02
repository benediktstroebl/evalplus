
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
    # get even and odd palindromes, then count them
    even_palindrome = [1, 2, 4, 6, 8]
    odd_palindrome = [3, 5, 7, 9, 11]
    even = odd = 0
    if n in even_palindrome:
        even += 1
    elif n in odd_palindrome:
        odd += 1
    else:
        start = 1
        while start <= n // 2:
            palindrome = str(start) + str(start)[::-1]
            if int(palindrome) % 2:
                odd += 1
            else:
                even += 1
            start += 1
    return even, odd
