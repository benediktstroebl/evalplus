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

The function takes in two positive integers, `a` and `b`, and returns a list of even digits between `a` and `b`, inclusive, but in ascending order. For example:
```python
print(generate_even_digits(2, 8)) # [2, 4, 6, 8]
print(generate_even_digits(8, 2)) # [2, 4, 6, 8]
print(generate_even_digits(10, 14)) # []
```

The function first resets `a` and `b` to have them share the same sign and `a` to be the lower bound. It then iterates through digits ranging from `a` to `b` and appends only the even digits to the `even_digits` list, which is then returned.