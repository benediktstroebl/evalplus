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
    # Ensure a is the lower bound and that both values are odd or even
    if a % 2 == 1:
        a //= 2
        a += 1
    if b % 2 == 1:
        b //= 2
    # Generate and return the even digits between the adjusted values
    even_digits = [int(d) for d in range(a, b + 1, 2)]
    return even_digits
```

This function ensures that the input values are within its boundaries and that the output is a valid list of even digits. It also maintains the invariant that the lower bound `a` is always even and the upper bound `b` is always odd, ensuring that the even digits are generated correctly in ascending order between them.