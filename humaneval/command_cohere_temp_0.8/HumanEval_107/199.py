Here's a Python script that includes a function to solve the given problem:
```python
def even_odd_palindrome(n):
    even, odd = 0, 0
    for i in range(1, n+1):
        s = str(i)
        if s == s[::-1] and int(s) % 2 == 0:
            even += 1
        elif s == s[::-1] and int(s) % 2 != 0:
            odd += 1
    return (even, odd)
```

The `even_odd_palindrome` function iterates through numbers from 1 to `n` and checks if each number is a palindrome. If it is, the variable `even` or `odd` is incremented based on whether the number is even or odd. Finally, the function returns a tuple containing the counts of even and odd palindromes.