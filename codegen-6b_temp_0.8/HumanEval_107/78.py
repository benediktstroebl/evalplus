
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
    total_even, total_odd = 0, 0

    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            total_even += 1

    for i in range(1, n + 1):
        if i % 2 == 1 and str(i) == str(i)[::-1]:
            total_odd += 1

    return total_even, total_odd

assert even_odd_palindrome(3) == (1, 2)
assert even_odd_palindrome(12) == (4, 6)
assert even_odd_palindrome(1) == (1, 0)
assert even_odd_palindrome(0) == (0, 0)

"""
    Dynamic Programming!
    We can use a 2D array to store the number of even and odd integer palindromes.
    For example, (2, 2) means there are only 2 even integer palindromes on one side, and 2 odd integer palindromes on the other side.
    (2, 0) means there are only 2 even integer palindromes on one side, and 0 odd integer palindromes on the other side.
    (0, 1) means there are only 0 even integer palindromes on one side, and 1 odd integer palindromes on the other side.
    (0, 0) means there are only 0 even integer palindromes on one side, and 0 odd integer palindromes on the other side.

    The tricky part is to jump from a state to another state using the information given in the array,
    from the corner states to the center state.

    Example:
        (2, 2):
            [0, 0][0, 0]
        then we are in the center state (i.e. (2, 2) / (1, 1))
        (2, 0):
            [0, 0][0, 1]
        then we jump from (2, 2) to (2, 1)
        (2, 1):
            [0, 1][0, 0]
        then we jump from (2, 1) to (1, 0)
        (1, 0):
            [0, 0][1