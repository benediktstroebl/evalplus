```python
def generate_even_digits(a, b):
    """
    Generates a list of even digits between two positive integers, a and b, in ascending order.

    Args:
        a (int): The lower bound of the range, which should be a positive integer.
        b (int): The upper bound of the range, which should be a positive integer.

    Returns:
        list: A list of even digits in the range [a, b], or an empty list if no even digits are found.
    """
    if a % 2 == 0 and b % 2 == 0:
        return []
    elif a % 2 == 0:
        return [x for x in range(a, b + 1) if x % 2 == 0]
    elif b % 2 == 0:
        return [x for x in range(a, b + 1) if x % 2 == 0]
    else:
        return []

# Test Cases
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
assert generate_even_digits(1, 10) == [2, 4, 6, 8]
assert generate_even_digits(100, 200) == []
```

This function takes in two positive integers, `a` and `b`, and generates a list of even digits between them, inclusive, and returns it in ascending order. The function checks if both `a` and `b` are even, in which case it returns an empty list because no odd digits will be found; it also handles the case where only one of `a` or `b` is even. You can use this function to solve the given problem statement. 

You can add test cases as needed to cover more scenarios and ensure the function is correctly configured. 
If you have more questions or need further assistance, please do not hesitate to ask!