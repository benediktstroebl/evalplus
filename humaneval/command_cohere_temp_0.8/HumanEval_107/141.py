Here's a Python script that includes a function to solve the given problem:
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
This script creates the `even_odd_palindrome` function, which serves the purpose of counting even and odd integer palindromes within the range(1, n). The function uses iterative logic to verify if each integer is a palindrome and then categorizes it as even or odd before returning a tuple containing both counts.