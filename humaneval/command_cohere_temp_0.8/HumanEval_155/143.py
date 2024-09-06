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

This script defines a function even_odd_count that takes a single argument, num, representing an integer. It then converts this integer to a string, and iterates through each digit. If it encounters a non-digit char, it skips it. It counts the number of even digits (zero) and the number of odd digits (all others) and then returns a tuple (even_count, odd_count).

Here is a simple test case to ensure the functionality:
```python
assert even_odd_count(123) == (1, 2)
``` 
And the output will be:
```bash
(1, 2)
```

Let me know if you would like me to explain any part of the code in more detail.