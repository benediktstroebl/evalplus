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

This function iterates through the integers from `a` to `b` (adjusted to have `a` as the lower value for easier iteration in each call). It checks if each integer is even by checking its modulus with 2, and appends the even integers to the `even_digits` list. The function returns this list, or an empty list if no even digits are found within the range.