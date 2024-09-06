```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))
```

This version of the code uses Python's built-in `range` function to generate a sequence of numbers up to `n` and then maps these to strings using `map`, joining the results together with spaces using `join`. This approach is more concise and efficient than using `enumerate` and `list comprehension`.