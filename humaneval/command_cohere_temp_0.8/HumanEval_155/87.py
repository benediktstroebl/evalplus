Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return number of even and odd digits in num."""
    num_str = str(num)
    even_count = 0
    odd_count = 0
    for char in num_str:
        if char > "9":
            continue
        elif char == "0":
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)
```

This script defines a function even_odd_count that takes a single argument, num, representing an integer. It then converts this integer to a string, and iterates through each digit. If it finds a digit larger than 9 (which would be characters like 'a' after conversion), it skips it. Otherwise, it increments the appropriate count variable, either even_count or odd_count, accordingly.

Finally, the function returns a tuple containing the calculated counts of even and odd digits.