```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): Start integer.
        b (int): End integer.

    Returns:
        list: List of even digits between a and b, in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracting even digits between a and b
    even_digits = [x for x in range(a, b + 1, 2) if x % 2 == 0]
    return even_digits

# Testing the function with various inputs.
test_cases = [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
]

for start, end, answer in test_cases:
    assert generate_even_digits(start, end) == answer
```

The function checks if `a` or `b` are odd or if `a` is greater than `b`, it returns `[]`.

Otherwise, it iterates through the even integers between `a` and `b` and returns them in ascending order. Test cases are provided to validate the function. You can add more tests to cover edge cases and verify it meets the problem requirements.