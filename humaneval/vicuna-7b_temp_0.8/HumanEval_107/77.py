
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
    # the range of integers that we want to check
    num_range = (1, n)
    # the set of even numbers
    even = set(num_range)
    # the set of odd numbers
    odd = set(range(2, n+1)) - set(num_range)
    # the number of even and odd palindromes respectively
    num_even = len(even)
    num_odd = len(odd)
    return (num_even, num_odd)