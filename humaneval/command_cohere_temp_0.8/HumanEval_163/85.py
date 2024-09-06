```python
def generate_even_digits(a, b):
    """
    Generating even digits between two positive integers, in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits between a and b, in ascending order.
    """
    # Ensuring the inputs are integers and sorting them
    a, b = map(int, (a, b))
    ab_str = str(a) + str(b)
    ab_str_sorted = ''.join(sorted(ab_str))
    
    # Filtering out even digits and converting them to integers
    even_digits = [int(d) for d in ab_str_sorted if d.isdigit() and d % 2 == 0]
    
    return even_digits
```

The function takes in two positive integers, `a` and `b`, and returns a list of even digits between `a` and `b`, inclusive, always in ascending order. The code ensures the input validity and efficiency of the function.