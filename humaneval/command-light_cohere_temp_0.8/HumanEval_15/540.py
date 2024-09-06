Here's a Python script that defines a function string_sequence with a self-contained docstring and tests:
```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 
    upto n inclusive.

    : Returns the sharable interface.

    Parameters:
    n: int (required)
        Desired string length.

    Returns: str containing space-separated numbers 
    from 0 to n, including n if n is 0.

    Test case:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
```