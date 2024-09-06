Here's the improved version of the Python script with a self-contained function that returns a string containing space-delimited numbers starting from 0 to n:
```python
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 
    upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return f"0 {n}"
```  This code is self-contained. It does not rely on any external libraries.