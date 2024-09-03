def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    :param n: int
    :return: tuple(even_palindrome, odd_palindrome)
    """
    even_palindrome = [i for i in range(1, n + 1) if i % 2 == 0]
    odd_palindrome = [i for i in range(1, n + 1) if i % 2 != 0]
    return even_palindrome, odd_palindrome