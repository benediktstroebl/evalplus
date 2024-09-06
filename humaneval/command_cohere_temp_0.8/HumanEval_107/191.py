Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've described:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The function takes a positive integer `n` as input and returns a tuple containing two integers representing the count of even and odd integer palindromes within the range `[1, n]`. The `str(i) == str(i)[::-1]` checks if a number is a palindrome by comparing the string representation of the number with its reverse.

The function then counts the number of even and odd palindromes and returns them as a tuple.