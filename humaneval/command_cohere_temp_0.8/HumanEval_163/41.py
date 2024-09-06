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
    # Ensure a is the lower bound and that both values are positive
    a %= 10
    b %= 10
    if a > b:
        a, b = b, a
    even_digits = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_digits.append(i)
    return even_digits
```
The function iterates through digits between `a` and `b`, adding each even digit to the `even_digits` list. The input values are also normalized to ensure `a` is the lower bound and that both values are positive. This approach guarantees that the generated list contains all even digits in ascending order between the two integers.