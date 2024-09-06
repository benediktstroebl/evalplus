Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and len(s) % 2 == 0:
            even_count += 1
        elif s == s[::-1] and len(s) % 2:
            odd_count += 1
        
    return (even_count, odd_count)
```

This function takes a positive integer `n` as input and returns a tuple containing two integers representing the count of even and odd-length palindromes in the range `[1, n]` using a single loop and some string manipulation.

The `range` function is used in Python to generate a sequence of numbers, and in this case, the loop goes from `1` to `n` (inclusive) to cover the scope of the problem. Using the loop, the function efficiently calculates the counts of even and odd palindromes and returns them as a tuple.