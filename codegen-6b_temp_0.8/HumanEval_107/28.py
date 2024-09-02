
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
    if n < 1:
        return [0, 0]

    if n == 1:
        return [0, 1]

    num_odd, num_even = 0, 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            num_even += 1
        else:
            num_odd += 1

        if is_palindrome(i):
            if i % 2 == 0:
                num_even -= 1
            else:
                num_odd -= 1

    return [num_even, num_odd]


assert even_odd_palindrome(1) == [0, 1]
assert even_odd_palindrome(2) == [0, 1]
assert even_odd_palindrome(3) == [0, 2]
assert even_odd_palindrome(4) == [1, 1]
assert even_odd_palindrome(5) == [1, 1]
assert even_odd_palindrome(6) == [1, 2]
assert even_odd_palindrome(7) == [1, 2]
assert even_odd_palindrome(8) == [1, 2]
assert even_odd_palindrome(9) == [0, 1]
assert even_odd_palindrome(10) == [0, 1]
assert even_odd_palindrome(11) == [1, 2]
assert even_odd_palindrome(12) == [4, 6]
assert even_odd_palindrome(13) == [4, 6]
assert even_odd_palindrome(14) == [4, 6]
assert even_odd_palindrome(15) == [4, 5]
assert even_odd_palindrome(16) == [4, 5]
assert even_odd_palindrome(17) == [4, 5]
assert even_odd_palindrome(18) == [4, 5]
assert even_odd_palindrome(19) == [4, 6]
assert even_odd_palindrome(20) == [4, 6]
assert even_odd_palindrome(21) == [1, 1]
