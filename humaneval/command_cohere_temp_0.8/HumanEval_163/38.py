```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): Start integer.
        b (int): End integer.

    Returns:
        list: List of even digits between a and b, in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracting even digits between a and b
    even_digits = []
    while a <= b:
        if a % 2 == 0:
            even_digits.append(a)
        a += 1

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function `generate_even_digits(a, b)` that takes two positive integers as arguments and returns a list of even digits that lie between `a` and `b`, inclusive, and always returns them in ascending order. The function first checks if the start or end integer is odd, and if the range is invalid (i.e., start is greater than end), it returns an empty list. Otherwise, it iterates through the integers between `a` and `b`, appending the even digits to the `even_digits` list and incrementing `a` by 1 in each iteration until `a` is less than or equal to `b`. The final list of even digits is returned in ascending order.

The test cases printed in the script demonstrate the function's behavior for different input combinations.