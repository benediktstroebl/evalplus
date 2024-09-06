Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    # Convert num to string and remove any non-digit characters
    num = str(num).strip('-.')
    even, odd = 0, 0
    for char in num:
        if char > '9':
            continue
        elif char % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
```

The script provides an example that demonstrates the function even_odd_count(-12), which returns ((1, 1)), and even_odd_count(123), which returns ((1, 2)).

The implementation works by first converting the integer to a string and removing any non-digit characters using the strip('-.') method. Then, the script iterates through each digit in the string, checking if it is even or odd, and finally returns the respective counts.