```python
def generate_integers(a, b):
    """
    Returns the even digits between a and b (inclusive).
    Assumes a and b are positive integers.

    Parameters:
    a (int): The lower bound of the range.
    b (int): The upper bound of the range.

    Returns:
    list: Even digits in the range [a, b], sorted in ascending order.
    """
    even_digits = []
    for n in range(a, b + 1):
        num_str = str(n)
        if int(num_str.even()) and not num_str.startswith('0'):
            even_digits.append(int(num_str))
    return sorted(even_digits)
```