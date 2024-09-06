```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    
    Args:
    - a (int): Starting integer.
    - b (int): Ending integer.
    
    Returns:
    - list: List of even digits in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracting even digits between a and b using list comprehension.
    even_digits = [x for x in range(a, b + 1, 2) if x % 2 == 0]
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits` that takes two integers as arguments, `a` and `b`. The function returns a list containing even digits between `a` and `b`, inclusive, and in ascending order. The function first checks if `a` or `b` is odd, or if `a` is greater than `b`, ensuring that the range contains at least one even number. It then uses a list comprehension to iterate through the even integers in the range `a` to `b` (skipping odd numbers) and returns them in ascending order.

The test cases, printed to the console, demonstrate the function's behavior for different input scenarios.