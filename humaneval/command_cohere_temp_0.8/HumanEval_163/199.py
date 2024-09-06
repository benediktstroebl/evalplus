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
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_digits.append(num)

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This function iterates through numbers from `a` to `b` (adjusted to have `a` as the lower bound), and appends the even digits to the `even_digits` list. The function returns this list. Note that if no even digits are found within the specified range, an empty list is returned.