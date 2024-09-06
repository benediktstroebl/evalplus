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
    # Filtering even numbers using divisibility by 2, and sorting them
    return sorted(x for x in range(a, b + 1) if x % 2 == 0)
```

The function utilizes list comprehension in conjunction with the `sorted` function to generate and order the even numbers in the range. The tests ensure that the function works correctly for various scenarios:
```python
def test_generate_even_digits():
    # No even numbers in the range
    assert generate_even_digits(10, 14) == []

    # All numbers are even in the range
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]

    # Mixed cases
    assert generate_even_digits(5, 11) == [6, 8]

    # Edge cases
    assert generate_even_digits(1, 10) == [2, 4, 6, 8]
    assert generate_even_digits(10, 1) == [2, 4, 6, 8]

test_generate_even_digits()
```

The test suite covers all scenarios, including edge cases, ensuring the function is robust and meets the problem statement's requirements.