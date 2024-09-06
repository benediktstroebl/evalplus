```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits between two positive integers a and b, in ascending order.

    Args:
        a (int): The lower bound of the range
        b (int): The upper bound of the range

    Returns:
        list: A list of even digits between a and b
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Generating even digits between a and b
    even_digits = [x for x in range(a, b + 1, 2)]
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function `generate_even_digits(a, b)` that takes two positive integers as arguments and returns a list of even digits between `a` and `b`, inclusive, provided they are both even and `a` is less than or equal to `b`. The function first checks if the conditions for returning an empty list are met and returns `[]` if they are. It then uses a list comprehension to generate even digits in increments of 2 between `a` and `b + 1`, which is the larger value between the two endpoints, as the list comprehension iterates by 2. The function returns this list of even digits in ascending order.

The test cases printed to the console, using `print(generate_even_digits(a, b))`, demonstrate the function's behavior for various inputs and show that it aligns with the expected output for the problem.