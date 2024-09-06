def count_palindromes(n):
    # Note: we could also iterate over int(n**2 / 2) to count odd palindromes
    even = 0
    odd = 0
    
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and len(s) <= n:
            if int(s) % 2 == 0:
                even += 1
            else:
                odd += 1
    return even, odd
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    even, odd = count_palindromes(n)
    return even, odd