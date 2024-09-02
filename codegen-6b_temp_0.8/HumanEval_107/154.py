
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
    result = (0, 0)
    for i in range(2, n + 1):
        count_odd = 0
        count_even = 0
        for x in range(1, i):
            if x & i == x:  # is divisible by i
                count_odd += 1
            if x & i != x: # not divisible by i
                count_even += 1
        if count_odd % 2 == 0:  # even count
            result = (result[0] + count_even, result[1] + 1)
        else:  # odd count
            result = (result[0] + count_even + 1, result[1] + 1)
    return result

assert even_odd_palindrome(3) == (1, 2)
assert even_odd_palindrome(12) == (4, 6)
assert even_odd_palindrome(7) == (3, 2)
assert even_odd_palindrome(25) == (32, 50)
assert even_odd_palindrome(15) == (1, 0)

