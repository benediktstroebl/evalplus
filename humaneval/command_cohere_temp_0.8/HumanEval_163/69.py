```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    evens = []
    for x in range(a, b + 1):
        if str(x).split('0')[1] == ''::
            evens.append(int(x))
    return evens

# Test cases
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
```

This script defines a function called `generate_even_digits` that searches for even digits in the range between two given integers (`a` and `b`). It does so by iterating through the range and checking if the current integer has an even digit. If it does, it's added to a list, which is then returned. The test cases ensure that the function behaves as intended for different scenarios.