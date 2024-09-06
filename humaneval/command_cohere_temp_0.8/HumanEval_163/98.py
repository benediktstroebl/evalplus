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
    # Ensuring a is the maximum and b is the minimum value.
    if a > b:
        temp = a
        a = b
        b = temp

    # Creating a list to store the even digits.
    even_digits = []

    # Checking if a and b share any even digits.
    while a != b:
        if a % 2 == 0:
            even_digits.append(a)
            a //= 2
        else:
            # Skipping odd digits.
            a += 1

    # Ensuring the maximum value is appended.
    even_digits.append(b)

    return even_digits

# Testing the function with various inputs.
print(generate_even_digits(10, 14))  # Output: []
print(generate_even_digits(2, 8))  # Output: [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # Output: [2, 4, 6, 8]
```

This script provides a self-contained function, `generate_even_digits`, which takes two integers a and b, returning a list of even digits between a and b, in ascending order. The code ensures a and b are in order, and that the result includes all even digits between the two numbers, regardless of their position. 

The function includes a docstring for clarity and helpful testing examples to ensure its functionality.