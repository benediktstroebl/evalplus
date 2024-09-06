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
    # Ensure a is the lower bound and b is the upper bound
    a, b = min(a, b), max(a, b)
    even_digits = []

    for digit in range(1, max(b.digits, a.digits) + 1):
        for num in range(a, b + 1, 10 ** digit):
            if int(num % 10) % 2 == 0:
                even_digits.append(num)

    return even_digits

# Test cases
a = 2
b = 8
print(generate_even_digits(a, b))  # Expected output: [2, 4, 6, 8]

a = 8
b = 2
print(generate_even_digits(a, b))  # Expected output: [2, 4, 6, 8]

a = 10
b = 14
print(generate_even_digits(a, b))  # Expected output: []
```

This Python script defines a function called `generate_even_digits`, which takes two positive integers, `a` and `b`, as arguments. The function generates a list of even digits that are present in the range between `a` and `b`, and ensures that the result is sorted in ascending order. The script includes test cases to validate the function's behavior against the expected outputs. Adjust the values of `a` and `b` in the test cases to match the problem's specified input ranges.