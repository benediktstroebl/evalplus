```python
def even_odd_count(num):
    """Return a tuple with counts of even and odd digits in 'num' respectively.

    Args:
        num (int): Target number.

    Returns:
        tuple: Even and odd digit counts.
    """
    even, odd = 0, 0
    num = abs(num)  # Ensure positive number
    digits = str(num)
    for digit in digits:
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
```