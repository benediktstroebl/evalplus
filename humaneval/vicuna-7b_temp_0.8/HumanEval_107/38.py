
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
    # check the input
    if n < 1 or n > 100:
        return -1

    # get the range of the input number
    low = 1
    high = n

    # get the odd palindromes
    odd_palindromes = [i for i in range(low, high + 1) if i % 2 == 1]

    # get the even palindromes
    even_palindromes = [i for i in range(low, high + 1) if i % 2 == 0]

    # check the number of even and odd palindromes
    num_even = len(even_palindromes)
    num_odd = len(odd_palindromes)

    return (num_even, num_odd)