
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
    if n <= 0: return None

    # find the upper bound
    upper_bound = int(str(n)[::-1])

    # find all the palindrome within (1, upper_bound]
    palindromes = [p for p in range(1, upper_bound + 1) if str(p) == str(p)[::-1]]

    # sort the palindrome
    palindromes = sorted(palindromes)

    # find even number and odd number of palindrome
    even_number = 0
    odd_number = 0
    for p in palindromes:
        if p % 2 == 0:
            even_number += 1
        else:
            odd_number += 1

    return even_number, odd_number

