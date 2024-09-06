Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
```python
def even_odd_palindrome(n):
    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        reversed_str = str(i)
        reversed_str = reversed_str[::-1]
        if int(reversed_str) == i:
            if len(reversed_str) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
```

This function takes a positive integer `n` as input and returns a tuple containing two counts: one for even-length integer palindromes and one for odd-length integer palindromes within the range `[1, n]`. The code demonstrates an efficient way to solve this problem by utilizing string manipulation and character reversal. 

The code has a straightforward logic and should run efficiently for values of `n` up to thousands without requiring complex algorithms or additional optimizations.  This approach prevents multiple iterations over the range and delivers a clean solution for the given problem.