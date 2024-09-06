
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
    # n = 3
    # 1. find all the even palindromes
    # 2. find all the odd palindromes
    # 3. return the number of even palindromes and odd palindromes

    def is_even_palindrome(n):
        str_n = str(n)
        return str_n == str_n[::-1]

    def is_odd_palindrome(n):
        str_n = str(n)
        return str_n[1:] == str_n[:len(str_n) - 1][::-1]

    even_palindromes = [i for i in range(n) if is_even_palindrome(i)]
    odd_palindromes = [i for i in range(n) if is_odd_palindrome(i)]
    return len(even_palindromes), len(odd_palindromes)

