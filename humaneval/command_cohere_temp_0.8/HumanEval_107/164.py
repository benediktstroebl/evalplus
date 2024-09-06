Here's a Python script that contains a function called `even_odd_palindrome` that solves the problem you've described:
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

The function takes a positive integer `n` as input and returns a tuple containing two integers representing the number of even and odd integer palindromes, respectively, that fall within the range from 1 to `n` (inclusive).

The `for` loop runs through the range from 1 to `n` and checks if each integer is a palindrome by comparing the string representation of the number with its reverse. If it is a palindrome and the number is even, the `even` count is incremented; otherwise, the `odd` count is incremented. The function finally returns a tuple of (even, odd).