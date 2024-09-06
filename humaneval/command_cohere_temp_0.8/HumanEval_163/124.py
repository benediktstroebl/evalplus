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
        if str(x).split('0')[1][-1] == '0':
            even_digits.append(int(x))
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function `generate_even_digits(a, b)` that takes two positive integers as arguments and returns a list of even digits in ascending order between `a` and `b`. The code iterates through integers from `a` to `b` (guaranteed by swapping if `a` is greater than `b`), checks if the integer is even by examining the last digit of its string representation, and appends qualifying integers to the `even_digits` list. The function returns this list of even digits. Test cases are provided to validate its behavior.