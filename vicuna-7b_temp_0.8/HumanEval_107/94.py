
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
    if n <= 10:
        return n, 0
    digits = [str(d) for d in str(n)]
    for i in range(1, len(digits)):
        if digits[i] == digits[0]:
            for j in range(i + 1, len(digits)):
                if digits[j] == digits[i] and digits[j-1] == digits[j]:
                    result = (1, 0)
                    for d in digits[:i]:
                        if d == digits[i] or d == digits[j]:
                            result = (result[0] + 1, result[1])
                            break
                    return result
    return (0, 1)
