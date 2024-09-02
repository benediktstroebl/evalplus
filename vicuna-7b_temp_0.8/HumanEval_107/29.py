
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
    # convert n to string
    n = str(n)
    # split the string into even and odd
    even_odd = [n[::2] + [n[1::2] if i == 1 else [n[0]] * 2 + n[2::2] if i == 0 else n[2::2] for i in range(len(n) // 2)]]
    # check if all elements in even are palindrome
    for i in range(len(even_odd)):
        if not all(c in str(i) for c in even_odd[i]):
            return -1
    # count the number of even palindrome
    even_palindromes = 0
    for i in range(len(even_odd) // 2):
        if i % 2 == 0:
            even_palindromes += len(even_odd[i])
    return (even_palindromes, len(even_odd) - even_palindromes)

