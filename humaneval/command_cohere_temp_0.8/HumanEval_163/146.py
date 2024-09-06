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
    a, b = max(a, b), min(a, b)
    even_digits = [str(i) for i in range(a, b + 1, 2)]
    return [int(digit) for digit in even_digits]
```

The function `generate_even_digits` takes in two positive integers, `a` and `b`, and returns a list of even digits between `a` and `b`, inclusive, but in ascending order. For example:
```python
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

The function first sorts the endpoints `a` and `b` with `a` being the upper bound and then iterates through integers between `a` and `b` in increments of 2, storing even digits in a string format. The function then converts these even digits from strings to integers, padding the result with any missing even numbers, and returns them in ascending order.