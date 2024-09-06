Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
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

This function takes in a positive integer `n` and returns a tuple with two elements: `even` and `odd`. These elements represent the number of even and odd integer palindromes, respectively, that fall within the range from 1 to `n` (inclusive).

The function uses a loop to iterate through all numbers from 1 to `n`. It checks if a number is a palindrome by converting it to a string and comparing it to its reverse. If it is a palindrome, the function checks its parity (even or odd) and increments the appropriate counter.

The provided examples and expected output are accurately described by the function and its comments.