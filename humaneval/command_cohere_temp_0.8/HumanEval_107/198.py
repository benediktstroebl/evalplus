Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've described:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and int(s) == int(s[::-1]):
            if len(s) % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function takes a positive integer `n` as input and aims to determine the count of even and odd integer palindromes within the range `[1, n]`. The function achieves this by iterating through all numbers from 1 to `n` and checking if each number is a valid integer palindrome. If it is, the count is incremented accordingly based on whether the length of its string representation is even or odd. The result is a tuple containing the counts of even and odd palindromes.