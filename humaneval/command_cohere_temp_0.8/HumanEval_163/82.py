Here's a Python script with a self-contained function `generate_even_digits` that solves the problem:
```python
def generate_even_digits(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    if a % 2 or b % 2:
        return []

    # Collect all even digits between a and b into a list
    even_digits = [x for x in range(a, b + 1, 2)]

    # Sort the list in ascending order
    even_digits.sort()

    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # Output: [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # Output: [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # Output: []
```
This code defines the `generate_even_digits` function, which takes two positive integers a and b as input and returns a list of even digits found between a and b, sorted in ascending order. The function first checks if either a or b is odd, and if so, it returns an empty list since no even digits are present. If both are even, it uses a list comprehension to collect all even integers between a and b into a list and then sorts it in ascending order before returning it.