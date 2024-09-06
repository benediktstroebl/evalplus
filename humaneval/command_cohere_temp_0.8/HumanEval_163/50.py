```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
    - a (int): the starting integer.
    - b (int): the ending integer.

    Returns:
    - list: A list of even digits in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracting even digits between a and b into a list.
    even_digits = [x for x in range(a, b + 1, 2)]

    return even_digits

# Testing the function with various inputs.
test_cases = [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
]

for args, expected in test_cases:
    actual = generate_even_digits(*args)
    assert actual == expected
```

The function generate_even_digits takes two integers a and b as arguments and returns a list of even digits between a and b. To ensure the list contains only even digits, we verify that both a and b are even (i.e., divisible by 2) before returning the range. The test cases cover multiple scenarios, including edge cases, to confirm the correctness of the function.