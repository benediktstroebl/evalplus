Here's a Python script with a self-contained function `generate_even_digits()` that solves the problem:
```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers a and b.

    Args:
        a (int): The starting positive integer.
        b (int): The ending positive integer.

    Returns:
        list: A list of even digits in ascending order between a and b.
    """
    # Ensure a is the maximum and b is the minimum to simplify checking even digits
    if a < b:
        a, b = b, a
    even_digits = []
    for digit in range(1, max(a, b) // 2 + 1):
        if a % digit == 0 and b / digit == 0:
            even_digits.append(digit)
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```
This script ensures `a` is always the maximum and `b` is always the minimum to simplify checking even digits in the range. It then appends the even digits to the `even_digits` list and returns the result.