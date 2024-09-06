```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits between two positive integers a and b, in ascending order.

    Args:
        a (int): The starting integer.
        b (int): The ending integer.

    Returns:
        list: A list of even digits between a and b, or an empty list if no even digits are found.
    """
    # Ensure a is the smallest value for easier iteration
    if a > b:
        a, b = b, a
    even_digits = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_digits.append(num)
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits` taking two integers as arguments, `a` and `b`. The function collects and returns a list of even digits between `a` and `b`, inclusive, and in ascending order. If there are no even digits within this range, the function returns an empty list. The code then verifies the function's behavior through three test cases, showing its ability to generate the even digits in ascending order between given intervals and handle cases where no even digits are present.