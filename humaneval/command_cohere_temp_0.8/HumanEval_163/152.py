```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
        a (int): The starting integer.
        b (int): The ending integer.

    Returns:
        list: A list of even digits from the range a to b, in ascending order.
    """
    
    # Ensuring a and b are sorted.
    a, b = min(a, b), max(a, b)
    even_digits = [int(d) for d in range(a, b + 1) if d % 2 == 0]
    return even_digits
```

This function takes two positive integers, `a` and `b`, and returns a list of even digits between `a` and `b`, inclusive, and in ascending order.

To ensure that the starting number isn't greater than the ending number, the function first sorts the two numbers using the `min` and `max` functions. Then, it uses a list comprehension with a generator expression to generate a list of even integers from `a` to `b` (inclusive). Finally, this list is returned. 

This solution is straightforward and efficiently solves the problem.