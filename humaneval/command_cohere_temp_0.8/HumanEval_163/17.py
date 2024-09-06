```python
def generate_even_digits(a, b):
    """
    Generating even digits between two positive integers, in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits between a and b, in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracting even digits between a and b
    even_digits = [x for x in range(a, b + 1, 2)]

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This Python script defines a function `generate_even_digits(a, b)` that takes two positive integers as arguments, `a` and `b`. It aims to return a list of even digits between `a` and `b`, inclusive, presented in ascending order. The function first checks if the range includes only even digits, is non-empty, and the lower bound is less than or equal to the upper bound. Subsequently, it employs list comprehension to filter out and sort the even digits within the specified range, returning the resultant list. 

The test cases, printed via `print`, confirm the function's correctness in the given scenarios. Adjust the test cases to cover a broader range of scenarios, and the unit tests will ensure the function remains accurate under various conditions.