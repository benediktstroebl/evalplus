
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
    # corner case
    if n == 0:
        return (0, 0)
    # hash set that stores even integer palindrome
    even_set = set()
    # hash set that stores odd integer palindrome
    odd_set = set()
    # iterate over even number range
    for i in range(1, n, 2):
        # if palindrome found, add it to the set
        if is_palindrome(i):
            even_set.add(i)
    # iterate over odd number range
    for i in range(1, n, 2):
        # if palindrome found, add it to the set
        if is_palindrome(i):
            odd_set.add(i)
    # return the length of the set
    return (len(even_set), len(odd_set))
