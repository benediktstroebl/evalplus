```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits between a and b.
    """
    # Ensure a is the lower bound
    if a > b:
        a, b = b, a
    even_digits = []
    for x in range(a, b + 1):
        if str(x).split('0')[1] % 2 == 0:
            even_digits.append(x)
    return even_digits
```

The function iterates through integers from `a` to `b`, and for each integer, it checks whether the digit immediately following the largest digit (to the right of the decimal point) is even. If it's even, the entire integer is added to the `even_digits` list.

The function ensures that `a` is indeed the lower bound and `b` is the upper bound by swapping them if `a` exceeds `b`. This covers the edge case mentioned in the statement. Ultimately, the function provides a list of even digits in ascending order between the two given integers.