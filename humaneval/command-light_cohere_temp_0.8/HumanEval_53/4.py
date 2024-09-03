```python
def add(x, y):  
    """
    Adds two numbers x and y and returns their sum.
    Args: x (int), y(int)  
    Returns: int 
    """
    return x + y

# Test the function
assertEqual(add(2,3), 5)
assertEqual(add(5,7), 12)
``` 
This code defines a function called `add` that takes two integers as arguments and returns their sum. It is using docstrings to provide a description of the function and its usage. The function is then tested using the `assertEqual` module to ensure its correctness.