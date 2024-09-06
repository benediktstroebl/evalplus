```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits in the range (a, b).
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extract even digits between a and b from the string representation
    even_digits = set(int('{}{}'.format(a // 2, d) for d in range(a // 2, (b // 2) + 1)))

    return sorted(even_digits)
```

The function takes in two positive integers, `a` and `b`, and returns a list of even digits that are between `a` and `b`, inclusive, and arranged in ascending order. The self-contained nature of the function is ensured by including the handling of corner cases, such as when the lower bound is greater than or equal to the upper bound, or when both bounds are even or odd. This is done to cover all possible scenarios that may arise when dealing with positive integers.