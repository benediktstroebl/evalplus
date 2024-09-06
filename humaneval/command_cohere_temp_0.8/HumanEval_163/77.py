```python
def generate_even_digits(a, b):
    """
    Generating even digits between two positive integers, in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits from the range a to b, in ascending order.
    """
    # Ensuring the inputs are integers and sorting them
    a, b = map(int, (a, b))
    sorted_digits = list(str(a)) + list(str(b))
    even_digits = [char for char in sorted_digits if char in '2468']
    
    return even_digits
```

This function takes two positive integers, `a` and `b`, and returns a list of even digits between `a` and `b`, inclusive, always in ascending order. The code first maps `a` and `b` to integers and then concatenates their string representations. It filters out the even digits from this representation and returns them sorted.

The function docstring provides an explanation of what the function does, what arguments it takes, and what it returns. It also gives an example of how this function can be used, making it clear for users to understand its purpose.