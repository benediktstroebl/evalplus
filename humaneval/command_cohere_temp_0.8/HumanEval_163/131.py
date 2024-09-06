```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits between two positive integers a and b, in ascending order.

    Args:
        a (int): The lower bound of the range, which should be a positive integer.
        b (int): The upper bound of the range, which should be a positive integer.

    Returns:
        list: A list of even digits that are present between a and b, in ascending order.
    """
    # Ensure a is the lower bound and that both a and b are even
    a, b = min(a, b), max(a, b)
    even_digits = [int for int in range(a, b + 1) if int % 2 == 0]
    return even_digits
```

The function takes in two positive integers, `a` and `b`, using them to generate and return a list of even digits that fall between `a` and `b` and are in ascending order. To ensure that the list contains only even digits, the function filters the range of numbers from `a` to `b` with a list comprehension that only includes even integers. To handle any cases where the input values are not in ascending order, the function sorts the values of `a` and `b` to ensure the correct range is covered.