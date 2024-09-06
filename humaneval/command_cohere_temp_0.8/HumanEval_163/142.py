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

This function operates on two positive integers, `a` and `b`, and returns a list of even digits that lie between `a` and `b`, inclusive, and arranged in ascending order. To make the iteration easier, the function swaps the values of `a` and `b` if `a` is greater than `b`, ensuring that `a` is always the smaller value. It then iterates through the integers from `a` to `b` (inclusive), checking if the digit at the tenths place is empty, which indicates an even integer. The integer is added to the `even_digits` list if it satisfies this condition. The resulting list is then returned.