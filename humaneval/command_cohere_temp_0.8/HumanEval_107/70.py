Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Ensure n is a positive integer
    n = abs(n)
    
    # Generate all integer palindromes from 1 to n
    pmns = [str(i) for i in range(1, n + 1)]
    pmns = [p for p in pmns if p == p[::-1]]
    
    # Count even and odd integer palindromes
    even_count = sum(1 for p in pmns if len(p) % 2 == 0)
    odd_count = sum(1 for p in pmns if len(p) % 2 == 1)
    
    return (even_count, odd_count)
```

This script generates all integer palindromes up to `n` and counts how many of them are even and how many are odd. It ensures that `n` is a positive integer by taking its absolute value, and it uses list comprehension for efficient palindrome generation and counting. The result is returned as a tuple of two numbers: the number of even and odd integer palindromes, respectively.