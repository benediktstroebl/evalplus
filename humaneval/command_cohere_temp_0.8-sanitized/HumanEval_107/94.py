def count_palindromes(n):
    # square and multiply to account for both directions
    odd = n * (n * n + 1) * 2
    even = n * n
    return even, odd
def even_odd_palindrome(n):
    return count_palindromes(n)