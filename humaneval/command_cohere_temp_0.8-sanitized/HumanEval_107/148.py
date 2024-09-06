def count_palindromes(n):
    # Count even palindromes
    even = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
    # Count odd palindromes
    odd = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 != 0:
                odd += 1
    return even, odd
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    return count_palindromes(n)