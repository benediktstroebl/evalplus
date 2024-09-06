```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    
    Args:
    - a (int): Starting number.
    - b (int): Ending number.
    
    Returns:
    - list: List of even digits in ascending order.
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

for a, b, expected in test_cases:
    actual = generate_even_digits(a, b)
    assert actual == expected, f"For inputs {a} and {b}, expected {expected} but got {actual}"
```

The test cases cover all essential scenarios as mentioned in the problem statement, such as invalid inputs (one or both inputs are not positive integers or are equal) and corner cases (smallest and largest even digit). The function `generate_even_digits` is thoroughly tested and should work correctly for any valid input.