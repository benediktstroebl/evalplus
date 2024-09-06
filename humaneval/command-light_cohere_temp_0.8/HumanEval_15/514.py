Here's a self-contained Python script with a function that generates a sequence of numbers in a markdown code block: 

```python
def string_sequence(n: int) -> str:
    """ 
    Returns a string containing space-delimited numbers starting from 0 to 
    n inclusive. 
    >>> string_sequence(0) 
    == '0'
    >>> string_sequence(5) 
    == '0 1 2 3 4 5'
    """
    return " ".join([str(i) for i in range(n)])
```