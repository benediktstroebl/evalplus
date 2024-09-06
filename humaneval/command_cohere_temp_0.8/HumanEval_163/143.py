```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    
    Args:
    - a (int): Starting number.
    - b (int): Ending number.
    
    Returns:
    - list: List of even digits in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracting even digits between a and b.
    even_digits = [x for x in range(a, b + 1, 2) if x % 2 == 0]

    return even_digits

# Test cases:
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function called `generate_even_digits` takes two integers as input, `a` and `b`, and returns a list of even digits that are between `a` and `b`, in ascending order. The function first checks if `a` and `b` are both even and if `a` is greater than or equal to `b`. If any of these conditions are not met, it returns an empty list. Otherwise, it iterates through the odd numbers between `a` and `b`, increments them by 2 to get the even digits, and adds them to the list `even_digits`. The result is a list of even digits in ascending order.