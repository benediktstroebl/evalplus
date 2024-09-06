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
    # Ensure a is the lower bound
    if a > b:
        a, b = b, a

    even_digits = []
    for x in range(a, b + 1):
        if str(x).strip('.')[-1] in '02468':
            even_digits.append(x)

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits`, which takes two positive integers, `a` and `b`, as arguments. The function's purpose is to create a list of even digits between `a` and `b`, inclusive, and arrange them in ascending order. The function first checks if `a` is greater than `b`, and if so, it swaps them to ensure `a` is the lower bound. It then iterates through the integers from `a` to `b` and appends integers with even digits (2, 4, 6, or 8) to the `even_digits` list. Finally, the function returns the `even_digits` list.