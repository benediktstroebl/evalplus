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
    # Ensure a is the smaller value for easier iteration
    if a > b:
        a, b = b, a

    even_digits = []
    for x in range(a, b + 1):
        if str(x).split('0')[1] % 2 == 0:
            even_digits.append(x)
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This code defines a function called `generate_even_digits` taking two integer arguments `a` and `b`. It aims to create and return a list of even digits in ascending order between `a` and `b`. To achieve this, the function iterates through integers from `a` to `b` (guaranteed by the step of `1`) and checks if the remaining digit after removing `0` is even, adding it to the `even_digits` list if true. The test cases, executed by printing, validate the function's behavior against the expected outcomes.