```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive. 
    >>> string_sequence(0) 
    -> ''
    >>> string_sequence(1) 
    -> '1'
    >>> string_sequence(5) 
    -> '0 1 2 3 4 5'
    >>> string_sequence(10) 
    -> ''
    >>> string_sequence(100) 
    -> '0 100 99 98 97 96 95 94 90 83 82 81 80 75 71 65 63 60 57 53 42 37 31'
    """

    if n == 0:
        return ''
    string_sequence = [f'{i}{str(i+1)}' for i in range(n)]
    return ' '.join(string_sequence)
```