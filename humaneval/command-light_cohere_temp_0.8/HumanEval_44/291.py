```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.

    :x: The number to be converted
    :type x: int
    :param base: The base to convert to
    :type base: int
    :return: string representation of x in base base
    """
    if base == 10:
        return str(x)
    elif 6 <= base <= 38:
        return f'{x:d}'
    else:
        raise ValueError(f"Invalid base {base}")

# tests
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (100, 2),
    (5, 5),
    (123, 7),
    # Add more test cases here as needed
]

for x, base in test_cases:
    result = change_base(x, base)
    print(f"Input: {x}, Base: {base}, Result: {result}")
```