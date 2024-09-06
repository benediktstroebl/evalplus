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
        if str(x).count('2', 1) % 2 == 0:
            even_digits.append(int(x))
    return even_digits
```

The function loops through numbers between `a` and `b`, checks if the number is even by examining the count of '2' in the string representation, and appends the even numbers to the `even_digits` list. The function now handles the case when `a` exceeds `b`, and returns the even digits in ascending order between the two given integers.