Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
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

This function takes a positive integer `n` as input and returns a tuple containing two counts: one for even-length integer palindromes and one for odd-length integer palindromes within the range `[1, n]`. The function uses a loop to iterate through all numbers from 1 to `n` and checks if each number is a palindrome. The len(s) % 2 condition is used to determine if the length of the string representation of the number has an even or odd length.

The function should work correctly for its given test cases considering the constraints provided where 1 <= n <= 10^3.