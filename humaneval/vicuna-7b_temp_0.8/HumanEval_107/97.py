
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
        if n % 2 == 0:
            return (n // 2, 0)
        else:
            return (0, n//2)
    else:
        result = []
        for i in range(1, n):
            if n % i == 0:
                result.append(n // i)
        result.extend([(n//i, 0) for i in range(1, n//2+1) if n//i % 2 == 0])
        result.append((0, n//2))
        return result
