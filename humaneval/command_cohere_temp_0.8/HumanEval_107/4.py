Here's a Python script that contains a function called `even_odd_palindrome` which solves the problem you've described:
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

This function iterates through numbers from 1 to `n` and checks if each number is a palindrome. The `str` and `int` conversions are used to determine if a number is a palindrome and if it is still an integer after converting it to a string and back to an integer. The function keeps track of the counts in the `even` and `odd` variables and returns a tuple of these counts.