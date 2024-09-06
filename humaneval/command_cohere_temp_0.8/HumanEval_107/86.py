Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for num in range(1, n+1):
        s = str(num)
        if s == s[::-1] and int(s) % 2 == 0:
            even += 1
        elif s == s[::-1] and int(s) % 2 != 0:
            odd += 1
    return (even, odd)
```

This function `even_odd_palindrome(n)` takes a positive integer `n` as input and calculates the number of even and odd integer palindromes within the range `[1, n]`. It uses two loops to iterate through all numbers from 1 to `n` and checks if each number is a palindrome and if it's even or odd. The count of even and odd palindromes is then returned as a tuple.