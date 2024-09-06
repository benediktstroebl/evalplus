```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 
    upto n inclusive.
    >>> string_sequence(0) 
    '0'
    >>> string_sequence(5) 
    '0 1 2 3 4 5'
    >>> string_sequence(10) 
    Traceback (most recent call last): 
      File "<ipythoninput>", line 5, in <module> : 
        ValueError: 'int' object has no attribute '__str__'
    """
    
    s = ''.join(str(i) for i in range(0, n+1))
    return s
```