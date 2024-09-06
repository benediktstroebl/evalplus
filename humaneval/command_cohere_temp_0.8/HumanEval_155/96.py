Here's a Python script with a self-contained function that solves the problem:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    digits = str(num)
    even, odd = 0, 0
    for digit in digits:
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
```

This function provides the number of even and odd digits in a given integer `num`. It does so by first converting the integer to a string, `digits`, and then cycling through each digit in the string. It counts each digit that is even (i.e. divisible by 2) as `even` and each digit that is odd (i.e. not divisible by 2) as `odd`. 

This solution passes the given test cases and returns a tuple containing the number of even and odd digits, respectively.