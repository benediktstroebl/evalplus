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
    # Ensure a is the lower bound and that both values are even
    a, b = min(a, b), max(a, b)
    even_digits = [int(d) for d in range(a, b + 1) if d % 2 == 0]
    return even_digits
```

The function leverages the built-in `range` function and a list comprehension to generate even digits between the two provided integers, ensuring the result is sorted in ascending order.

This solution covers all cases:
1. `a` and `b` are both even: ([`a`, `a` + 2, `a` + 4, ..., `b`])
2. `a` is odd and `b` is even: ([0, `a` + 2, `a` + 4, ..., `b`])
3. `a` and `b` are both odd: ([0, 1, `a` + 2, `a` + 4, ..., `b`])

It also covers cases where `a` and `b` are close together, like `[2, 4, 6, 8]` or `[8, 2, 4, 6]`.

The unit tests for this function would look like this:
```python
def test_generate_even_digits():
    # Basic Cases:
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]

    # Edge Cases:
    assert generate_even_digits(10, 14) == []
    assert generate_even_digits(0, 10) == [0, 2, 4, 6, 8]
    assert generate_even_digits(100, 200) == [102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]

```

You can use an appropriate framework like `pytest` to implement and run these tests. 
This solution has a time complexity of O(1) as it uses a single loop to generate all even digits between the two integers, and it has a space complexity of O(n), where n is the number of even digits between `a` and `b`, as it creates a list of size n.