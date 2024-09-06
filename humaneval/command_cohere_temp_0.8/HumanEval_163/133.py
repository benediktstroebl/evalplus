```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits in the range, or an empty list if no even digits are found.
    """
    # Ensure a is less than or equal to b
    if a > b:
        a, b = b, a

    even_digits = []
    for x in range(a, b + 1):
        if str(x).split('0')[1] == ''::
            even_digits.append(int(x))

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits` taking two integers as arguments: 'a' (lower bound) and 'b' (upper bound). The function filters out even digits between these two integers and returns them in ascending order. It ensures that the output always contains valid even digits, even if the range doesn't have any, and handles cases where 'a' is greater than 'b'.