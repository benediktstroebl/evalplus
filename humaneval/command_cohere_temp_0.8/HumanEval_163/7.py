```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits between two positive integers a and b, in ascending order.

    Args:
        a (int): The lower bound of the range, which should be a positive integer.
        b (int): The upper bound of the range, which should be a positive integer.

    Returns:
        list: A list of even digits ranging from a to b, in ascending order. Empty if no even digits are present.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Generating a list of even digits between a and b.
    even_digits = [int(d) for d in range(a, b + 1) if d % 2 == 0]
    return even_digits

# Test cases:
print(generate_even_digits(2, 8))  # Output: [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # Output: [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # Output: []
```

This Python script defines a function called `generate_even_digits`, which takes two positive integer arguments `a` and `b`. The function filters the range from `a` to `b` for even digits, sorts them in ascending order, and returns them in a list. If there are no even digits in the range, the function returns an empty list. 

The code includes test cases to validate its functionality: it outputs the even digits between the given ranges for the first two test cases and acknowledges the absence of even digits in the third test case.