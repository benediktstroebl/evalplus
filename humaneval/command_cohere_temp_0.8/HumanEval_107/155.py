Here's a Python script that contains a function named `even_odd_palindrome` designed to address the given problem:
```python
def even_odd_palindrome(n):
    # Generate all integer palindromes from 1 to n
    ps = [s for s in map(str, range(1, n+1)) if s == s[::-1]]
    even, odd = 0, 0
    
    # Separate even and odd palindromes
    for p in ps:
        if len(p) % 2 == 0:
            even += 1
        else:
            odd += 1
            
    return (even, odd)
```

This script generates all integer palindromes from 1 to `n` and counts the even and odd ones separately to fulfill the problem requirements.