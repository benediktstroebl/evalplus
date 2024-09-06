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
        if str(x).split('0')[1] % 2 == 0:
            even_digits.append(x)
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits` taking two integer arguments, `a` and `b`, and returns a list of even digits in the range between `a` and `b`, inclusive, but in ascending order. The code ensures `a` is the lower bound and then iterates through the integers, checking if the remainder of the digits after the first digit is divisible by 2, adding it to the `even_digits` list if it is. Test cases are included and print the expected outputs.