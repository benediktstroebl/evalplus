```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits from the first to the last number given a range.

    Args:
        a (int): The first number of the range.
        b (int): The last number of the range.

    Returns:
        list: A list of even digits from the first to the last number in the range.
    """
    if a % 2 == 0 and b % 2 == 0:
        list_of_even = [int(x) for x in range(a, b + 1) if x % 2 == 0 and x <= b]
        return list_of_even
    else:
        return []
```

The function takes in two positive integers, `a` and `b`, and returns a list of even digits from the first to the last number in the range between `a` and `b`. The code tests if both `a` and `b` are even, and if so, it generates the even digits between them in ascending order, returning the list.

Here is a simple test suite that can be added to verify the functionality:
```python
def test_generate_even_digits():
    # Basic Test
    assert generate_even_digits(10, 14) == []
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]

    # Edge Cases
    assert generate_even_digits(1, 11) == [2, 4, 6, 8]
    assert generate_even_digits(0, 100) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert generate_even_digits(25, 26) == []

test_generate_even_digits()
```

This test suite includes multiple tests to cover different cases of input for the `generate_even_digits` function.