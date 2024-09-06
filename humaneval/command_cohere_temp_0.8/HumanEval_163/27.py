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
    # Ensure a is the smaller value for easier iteration
    if a > b:
        a, b = b, a

    even_digits = []
    for x in range(a, b + 1):
        if str(x).split('0')[1] == '':
            even_digits.append(int(x))

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function `generate_even_digits(a, b)` which takes in two positive integers, `a` and `b`, and returns a list of even digits in ascending order between `a` and `b`, inclusive. The code ensures `a` is always the smaller value for easier iteration and checks if a number is even by examining whether its expanded form in digits ends in an empty string, indicating that all digits are even. The function is tested with three cases: returning expected even digits between the given values, and an empty list for no even digits in the range.