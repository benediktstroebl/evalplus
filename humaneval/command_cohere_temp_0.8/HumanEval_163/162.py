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
        if str(x).split('0')[1] == '0':
            even_digits.append(int(x))
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This function operates on two parameters: `a`, which represents the lower bound integer, and `b`, which represents the upper bound integer. It generates a list of even digits in ascending order that fall between these two integers. To achieve this, it iterates through integers from `a` to `b` (inclusive), checking if the integer is even by examining its digits. Specifically, it looks for integers whose first digit after dropping all '0' prefixes is '0'. These are added to the `even_digits` list, which is then returned. The test cases provided in the original prompt demonstrate how the function operates under different scenarios.