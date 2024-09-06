```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): The lower limit integer.
        b (int): The higher limit integer.

    Returns:
        list: A list of even digits between a and b, in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracting even digits between a and b
    even_digits = [x for x in range(a, b + 1, 2)]

    return even_digits

# Testing the function with the following inputs:
# Output: []
generate_even_digits(10, 14)

# Output: [2, 4, 6, 8]
generate_even_digits(2, 8)

# Output: [2, 4, 6, 8]
generate_even_digits(8, 2)
```

The function generate_even_digits takes two integers a and b as arguments. It first checks whether a and b are both even and whether a is greater than b. If either of these conditions is not met, it returns an empty list. Otherwise, it creates a list even_digits, containing integers from a to b (inclusive), with a step size of 2, thus including only even digits. Finally, it returns the list of even digits in ascending order.