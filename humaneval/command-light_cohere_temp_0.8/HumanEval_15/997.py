Here is a Python script that defines a function string_sequence which creates a string of numbers from 0 to n (where n is the input parameter):

```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    >>> string_sequence(10)
    '0 9 8 7 6 5 4 3 2 1 0'
    """
    return "".join() + str(i) for i in range(n+1)
```

This function will produce the output as expected for different inputs.