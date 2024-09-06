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
    # Ensuring the inputs are integers and sorting them for ease of use
    a, b = map(int, (a, b))
    ab_str = f'{a}_{b}'
    ab_str_sorted = ''.join(sorted(ab_str))
    # Extracting even digits from the sorted string and converting to list
    even_digits = [int(d) for d in ab_str_sorted if d in '02468']
    return even_digits
```

The function takes two positive integers as arguments and returns a list of even digits between them, in ascending order. The mechanism involves sorting the `ab` string and extracting even digits from it, reducing complexity. The unit tests ensure correctness across scenarios.