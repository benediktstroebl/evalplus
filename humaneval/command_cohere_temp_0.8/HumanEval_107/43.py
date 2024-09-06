Here's a Python script that includes a self-contained function to solve the problem of counting even and odd integer palindromes within a given range:
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

This function iterates through numbers from 1 to `n` and checks if each number is a valid integer palindrome. If it is, the function increments the appropriate counter (`even` or `odd`) depending on whether the length of the palindrome is even or odd. The function then returns a tuple containing the counts of even and odd integer palindromes.