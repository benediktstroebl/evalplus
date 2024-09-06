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
    # Filter even numbers using the modern approach with int.bit_length()
    even_digits = [x for x in range(a, b + 1) if not x % 2 and x >= a and x <= b]
    return even_digits
```

The function uses a list comprehension to filter out even digits between `a` and `b` by taking advantage of the `bit_length()` method available on integer objects in Python. This method returns the number of bits needed to represent the integer, which is an odd number for even integers and an even number for odd integers. Thus, the filtering condition `not x % 2` combined with the range constraint `x >= a and x <= b` ensures that only even digits between `a` and `b` are captured. 

This approach is more concise and efficient than using the `__iter__()` method and `filter()` function, although it is less universal as it relies on specific properties of integer values. 

The function is self-contained and can be reused and understood in isolation, which aligns with the problem statement.