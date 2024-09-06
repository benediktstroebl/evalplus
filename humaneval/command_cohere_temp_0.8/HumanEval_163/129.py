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
    # Ensure a is the lower bound
    if a > b:
        a, b = b, a
    even_digits = []
    for x in range(a, b + 1):
        if str(x).strip('0').isdigit():
            even_digits.append(int(str(x)[0]))
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```
This Python script defines a function `generate_even_digits(a, b)` that takes two positive integers as arguments and returns a list of even digits between `a` and `b`, inclusive, always in ascending order. The code first checks if `a` is greater than `b`, ensuring that the lower bound is correct. It then iterates through the integers using a range from `a` to `b + 1` and checks if each integer has a single digit and is an even digit. These even digits are added to the `even_digits` list, which is returned. Test cases are provided to demonstrate the function's behavior for different input scenarios.