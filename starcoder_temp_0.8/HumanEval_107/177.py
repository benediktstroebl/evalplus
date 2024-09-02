
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

    if n <= 1:
        return (0, 0)

    def count_all_palindromes(start, end):
        count = 0
        for i in range(start, end + 1):
            if str(i) == str(i)[::-1] and i > 9:
                count += 1

        return count

    even, odd = 0, 0
    for i in range(1, n + 1):
        if i < 10:
            odd += 1 if i % 2 == 1 else 0
            even += 1 if i % 2 == 0 else 0
        elif i < 100:
            odd += 1 if i % 2 == 1 else 0
            even += 1 if i % 2 == 0 else 0
            odd += count_all_palindromes(10, i)
            even += count_all_palindromes(10, i)
        elif i < 1000:
            odd += 1 if i % 2 == 1 else 0
            even += 1 if i % 2 == 0 else 0
            odd += count_all_palindromes(10, i)
            even += count_all_palindromes(10, i)
            odd += count_all_palindromes(100, i)
            even += count_all_palindromes(100, i)

    return even, odd

