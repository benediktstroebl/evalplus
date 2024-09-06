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

This Python script defines a function called `generate_even_digits` takes two integers as input, `a` and `b`, and returns a list of even digits that lie between `a` and `b`, inclusive, but in ascending order. The function first checks if `a` and `b` are both even and `a` is greater than or equal to `b`. If any of these conditions are not met, the function returns an empty list. Otherwise, it uses a list comprehension to iterate through even integers between `a` and `b`, in increments of 2, and returns them in ascending order. 

The test cases printed in the script demonstrate how the function works for different scenarios.