Here's a Python script with a self-contained function `generate_even_digits` that solves the problem statement and includes corresponding unit tests:
```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers a and b, in ascending order.

    Parameters:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits in the range, or an empty list if no even digits are found.
    """
    if a % 2 or b % 2 or a > b:
        return []

    even_digits = []
    while a <= b:
        if a % 2 == 0:
            even_digits.append(a)
        a += 1

    return even_digits

def test_generate_even_digits():
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]
    assert generate_even_digits(10, 14) == [12, 14]
    assert generate_even_digits(1, 10) == [2, 4, 6, 8]
    assert generate_even_digits(100, 200) == []

if __name__ == "__main__":
    test_generate_even_digits()
```

In this script, the `generate_even_digits` function accepts two positive integers, `a` and `b`, and returns a list of even digits between them. The unit test, `test_generate_even_digits`, validates the function's correctness across different scenarios. When executed directly (not imported), the script runs the unit tests.