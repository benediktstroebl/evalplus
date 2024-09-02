
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
    num_even = 0
    num_odd = 0

    for num in range(1, n + 1):
        num_str = str(num)
        if num_str == num_str[::-1]:
            if num_str.endswith('0') or num_str.endswith('2') or num_str.endswith('4') \
                    or num_str.endswith('6') or num_str.endswith('8'):
                num_even += 1
            else:
                num_odd += 1

    return num_even, num_odd
