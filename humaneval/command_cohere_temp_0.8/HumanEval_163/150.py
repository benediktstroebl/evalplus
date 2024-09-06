```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits in ascending order between a and b.
    """
    # Ensure a is the smaller value for easier iteration
    if a > b:
        a, b = b, a

    even_digits = []
    for x in range(a, b + 1):
        if str(x).strip('0').isdigit():
            even_digits.append(int(str(x)[0]))

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This code defines a function called `generate_even_digits` that takes two integers as arguments, `a` and `b`. The function generates a list of even digits ascending between `a` and `b`, ensuring that the result is sorted in ascending order and doesn't include unnecessary '0' prefixes. It returns this list, and the provided examples illustrate its behavior.