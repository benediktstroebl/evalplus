
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
    assert 1 <= n <= 10**3

    # helper to check if an integer is palindrome
    def is_palindrome(n):
        return n == int(str(n)[::-1])

    # helper to check if an integer is even
    def is_even(n):
        return not n % 2

    # helper to get all the palindromes within a range
    def get_palindromes(n):
        palindromes = []
        for i in range(n, 0, -1):
            for j in range(i, 0, -1):
                curr = i * j
                if curr < n:
                    break
                if is_palindrome(curr) and is_even(curr):
                    palindromes.append(curr)

        return palindromes

    # calculate the number of even and odd palindromes
    palindromes = get_palindromes(n)
    return (palindromes.count(True), palindromes.count(False))

