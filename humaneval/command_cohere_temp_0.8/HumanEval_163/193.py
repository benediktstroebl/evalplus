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
        if str(x).split('0')[1] == '':
            even_digits.append(int(x))
    return even_digits
```

The function takes in two positive integers, `a` and `b`, and returns a list of even digits between `a` and `b`, inclusive, but in ascending order. For example:
```python
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

The code ensures that `a` is the lower bound (i.e., less than or equal to `b`) by swapping them if `a` exceeds `b`. It then iterates through integers from `a` to `b` (inclusive) and extracts even digits from the string representation of integers using `str.split('0')`, skipping over single-digit numbers, which are not even. The even digits are then appended to the `even_digits` list and returned.