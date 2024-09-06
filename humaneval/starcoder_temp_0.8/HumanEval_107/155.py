
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
    # if n is odd
    if n % 2:
        # set odd palindromes
        odd_palindromes = 0
        # count odd palindromes
        for i in range(1, n + 1, 2):
            # make a string from i and reverse it
            tmp = str(i)
            tmp = tmp[::-1]
            # if it is palindrome, count it
            if tmp == tmp[::-1]:
                odd_palindromes += 1
        # return the result
        return odd_palindromes, odd_palindromes

    # if n is even
    else:
        # set even palindromes
        even_palindromes = 0
        # count even palindromes
        for i in range(0, n + 1, 2):
            # make a string from i and reverse it
            tmp = str(i)
            tmp = tmp[::-1]
            # if it is palindrome, count it
            if tmp == tmp[::-1]:
                even_palindromes += 1
        # return the result
        return even_palindromes, even_palindromes

