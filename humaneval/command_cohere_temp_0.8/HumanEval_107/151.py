Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
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

The function takes a positive integer `n` as input and returns a tuple containing two integers representing the number of even and odd integer palindromes, respectively, that fall within the range from 1 to `n` (inclusive).

The `even_odd_palindrome` function iterates through numbers from 1 to `n` and checks if each number is a valid integer palindrome. If it is, the function increments the appropriate counter (`even` or `odd`) depending on whether the length of the string representation of the number is even or odd. Finally, the function returns a tuple containing the counts of even and odd palindromes.