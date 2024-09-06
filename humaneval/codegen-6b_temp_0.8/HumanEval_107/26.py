
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
    if n <= 0:
        return 0, 0

    def dfs(number, count_even, count_odd, visited):
        if number in visited:
            return count_even, count_odd
        if number == 1:
            return count_even, count_odd
        visited.add(number)

        if number % 2:
            count_odd += 1
        for c in range(1, 10):
            if (number % 10 != c and number // 10 % 10 != c) or (number % 10 == c and number // 10 % 10 == c):
                count_even, count_odd = dfs(number * 10 + c, count_even, count_odd, visited)
        return count_even, count_odd

    visited = set()
    even, odd = 0, 0
    for c in range(1, 10):
        even, odd = dfs(c, even, odd, visited)
    return even, odd
