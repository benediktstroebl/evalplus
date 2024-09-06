```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 up to n.
    >>> '0' in string_sequence(0)
    True
    >>> ''.join" in string_sequence(5)
    False
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    >>> list(string_sequence(6))
    [0,1,2,3,4,5,6]
    """
    if n == 0:
        return '0'
    else:
        numbers = [0]
        for i in range(1, n+1):
            numbers.append(numbers[-1]+1)
        return ' '.join(str(x) for x in numbers)
```