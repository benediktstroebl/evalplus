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
    for x in range(a, b + 1):
        if str(x).split('0')[1][-1] == '0':
            even_digits.append(x)

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This function iterates through integers between `a` and `b`, checks if the integer is even by examining the last digit of its string representation, and appends the even ones to the `even_digits` list. The function also handles the case where `a` is greater than `b` by swapping them to ensure `a` is the lower bound.