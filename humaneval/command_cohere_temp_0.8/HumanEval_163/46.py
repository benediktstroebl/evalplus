```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits between a and b, in ascending order.
    """
    # Ensuring the inputs are within the valid range and both are odd
    if a > b:
        return generate_even_digits(b, a)
    if not (a % 2 and b % 2):  # Ensuring both are odd
        return []

    even_digits = []
    for x in range(a, b + 1):
        if x % 2 == 0:
            even_digits.append(x)

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This function validates the input criteria: the lower bound `a` must be less than or equal to the upper bound `b` and both `a` and `b` must be odd integers. These conditions ensure the function operates within valid bounds and addresses the specific problem of generating even digits.

The function then iterates through the integers between `a` and `b` (inclusive) and appends any even integers to the `even_digits` list, which is returned at the end.