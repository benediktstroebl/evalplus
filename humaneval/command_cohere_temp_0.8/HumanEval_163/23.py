```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    numbers = [str(i) for i in range(a, b + 1)]
    even_digits = [int(i) for i in numbers if i % 2 == 0]
    return even_digits

# Test Cases
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
```

This code defines the `generate_even_digits()` function, taking two integers `a` and `b` as arguments, presumably starting index and ending index to fetch even digits between them. It first creates a list of strings `numbers` representing integers from `a` to `b` (inclusive). Then, it filters `numbers` to create `even_digits`, a list of integers containing the even digits. The function returns this `even_digits` list.

The test cases, assuming to be executed using the `assert` statement, verify the function's behavior for the given examples, ensuring the correct even digits are returned.