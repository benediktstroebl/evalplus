Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've outlined:
```python
def even_odd_palindrome(n):
    # Generate all integer palindromes from 1 to n
    ps = [s for s in map(str, range(1, n+1)) if s == s[::-1]]
    even, odd = 0, 0
    
    # Count and return the count of even and odd palindromes
    for p in ps:
        if int(p) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
```

This script generates all integer palindromes up to `n` and counts how many of them are even and how many are odd, then returns the respective counts in a tuple. 

The `range(1, n+1)` list of integers is converted to strings (`map(str, ...)`), and then converted to lists of characters, appending each character to itself to create potential palindromes. The `s == s[::-1]` condition checks if the string is a palindrome. 

The counts are accumulated in the `for` loop and then returned as a tuple. 

There is also a comment in the code that explains the logic and the purpose of the different steps, so it should be understandable to disregard the given explanation and use the code as a standalone solution. 

This solution should work seamlessly for the given problem statements and their intended test cases.