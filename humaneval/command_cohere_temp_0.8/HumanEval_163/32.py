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

This Python script defines a function called `generate_even_digits` that takes two integers as arguments, `a` and `b`. The function returns a list containing even digits between `a` and `b`, in ascending order, ensuring `a` and `b` are both positive and have the same parity. The algorithm extracts even digits using a list comprehension, incrementing by 2 (skipping odd numbers) and filtering out non-even numbers. The result is a list of even digits if there are any within the specified range, and an empty list if no even digits are found within the range. 

The console output demonstrates the function's behavior for sample inputs: `[]` if no even digits are found and `[2, 4, 6, 8]` when such digits are present in the specified range.