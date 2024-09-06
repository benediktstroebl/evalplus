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
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_digits.append(num)
    return even_digits
```

The function takes in two positive integers, `a` and `b`, and returns a list of even digits that are between `a` and `b`, inclusive, and sorted in ascending order. The test cases are:
```python
def test_generate_even_digits():
    # Basic Cases:
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]
    assert generate_even_digits(10, 14) == [12, 14]

    # Edge Cases:
    assert generate_even_digits(20, 24) == [22, 24]
    assert generate_even_digits(10, 10) == [10]
    assert generate_even_digits(5, 5) == []

    # Test Dependency on Args:
    assert generate_even_digits(3, 7) == [6]
    assert generate_even_digits(7, 3) == [2, 4, 6]

test_generate_even_digits()
```

The test cases cover a variety of scenarios, including basic cases, edge cases, and cases that test the dependency on the input arguments.