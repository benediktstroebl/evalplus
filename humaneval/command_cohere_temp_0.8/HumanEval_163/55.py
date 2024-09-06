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
    # Checking if range is valid and there are no even digits
    if not (a % 2 and b % 2 and a <= b):
        return []

    # Generating and sorting the even digits between a and b
    even_digits = [x for x in range(a, b + 1, 2)]
    return sorted(even_digits)
```
The function utilizes Python's range and list comprehensions to efficiently determine the even digits between the two input numbers, and the sorting function to arrange them in ascending order.

To ensure the function handles edge cases, the input checks verify if the range is valid and there are no even digits to return. In certain scenarios, these checks also determine empty lists to be returned. 

This function is adaptable and can be of use in various scenarios that require even digits to be generated or analyzed.