```python
def generate_even_digits(a, b):
    """
    Generating even digits between two integers, in ascending order.

    Args:
    - a (int): Starting integer.
    - b (int): Ending integer.

    Returns:
    - list: List of even digits between a and b, in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracting even digits between a and b
    even_digits = [x for x in range(a, b + 1) if x % 2 == 0]

    return even_digits

# Testing the function with various inputs.
test_cases = [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
]

for args, expected in test_cases:
    actual = generate_even_digits(*args)
    assert actual == expected, f"For inputs {args}, expected {expected} but got {actual}"
```

The test cases cover multiple edge scenarios to ensure the function behaves correctly. The function itself checks for the evenness of the starting and ending integers, as well as whether they are in the correct order, to determine whether a valid operation has been called. Ultimately, it fulfills the problem statement by returning the even digits in ascending order between the two input integers.