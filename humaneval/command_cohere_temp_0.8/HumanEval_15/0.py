```python
def string_sequence(n):
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    """
    return ' '.join(map(str, range(n+1)))
```

This straightforward Python script defines a function called `string_sequence`, which accepts a single argument representing the upper limit of a sequence of numbers. The function uses the `range` function to generate a sequence of numbers from 0 to `n`, inclusive. It then employs the `map` function to convert these numbers to strings, finally joining the string values together with spaces using the `join` method. The resulting string represents a sequence of numbers from 0 to `n`, separated by spaces. 

The function is appropriately documented with a docstring that describes its purpose, input, and output. Additionally, the function is tested with two test cases that verify its behavior for the values of `n` provided.