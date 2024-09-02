
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
    # 1 <= n <= 10^3
    n = int(n)
    # one is the number of odd integer palindromes
    one = 0
    # two is the number of even integer palindromes
    two = 0
    # starting from 2 to n-1, check if the number is a palindrome
    for i in range(2, n):
        # if the number is a palindrome
        if i % 2 == 0:
            # increment even count
            two += 1
        else:
            # increment odd count
            one += 1
    return (two, one)
