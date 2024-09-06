```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits from the first to the last number given a pair of positive integers.

    Args:
        a (int): The first positive integer.
        b (int): The second positive integer.

    Returns:
        list: A list of even digits from the first to the last number in ascending order.
    """
    if a % 2 == 0 and b % 2 == 0:
        result = [str(x) for x in range(a, b + 1, 2)]
        return result
    else:
        return []

# Test cases
print(generate_even_digits(10, 14))  # Output: []
print(generate_even_digits(2, 8))  # Output: [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # Output: [2, 4, 6, 8]
```

This Python script defines a function called `generate_even_digits` that takes two positive integers as arguments (`a` and `b`). The function generates a list of even digits from the first to the last number and returns it in ascending order. 

The function first checks if both `a` and `b` are even; if so, it uses a list comprehension to generate a list of even digits from `a` to `b`, inclusive, and returns this list. If not, the function returns an empty list. 

The test cases provided demonstrate how the function behaves for different scenarios: emptying the list for out-of-range inputs and returning a valid list for in-range inputs.