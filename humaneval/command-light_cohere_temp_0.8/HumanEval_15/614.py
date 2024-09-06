Here's a self-contained Python script with a function that generates a sequence of numbers in a markdown code block:

```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    >>> string_sequence(10)
    '0 9 8 7 6 5 4 3 2 1'
    >>> print_sequence(string_sequence(20))
    '0 19 18 17 16 15 14 13 12 10 9 8 7 6 5 4 3 2 1'
    """
    return ''.join(str(i) for i in range(0, n+1))
def print_sequence(s: str) -> None:
    print(s)
```