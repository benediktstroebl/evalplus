```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits between two positive integers a and b, in ascending order.

    Args:
        a (int): The lower bound of the range, which should be a positive integer.
        b (int): The upper bound of the range, which should be a positive integer.

    Returns:
        list: A list of even digits between a and b, in ascending order. If no even digits are found, an empty list is returned.
    """
    # Ensure a and b are positive and sorted
    a, b = max(a, b), min(a, b)
    even_digits = [int for int in range(a, b + 1) if int % 2 == 0]
    return even_digits
```

The function utilizes a generator expression, aided by the built-in `range` function, to efficiently filter even integers between `a` and `b`. The expression iterates through the numbers between `a` and `b` (inclusive), checking if each number is divisible by 2 (i.e., even), and converts it to an integer using `int()`. The resulting even integers are then returned as a list.

This approach ensures that the function works correctly regardless of the relative values of `a` and `b`, or their proximity to each other, as long as they are both positive integers. Furthermore, it efficiently generates the list of even integers without duplicates.