def count_palindromes(n):
    # Square the number to make it even if it is odd
    count_odd = sum(1 for i in range(1, n+1) if int(str(i)**2) == i)
    # Remove the square root to make it odd if it is even
    count_even = sum(1 for i in range(1, n+1) if int(str(i)**0.5) == i) - int(n**0.5)
    return (count_even, count_odd)
def even_odd_palindrome(n):
    return count_palindromes(n)