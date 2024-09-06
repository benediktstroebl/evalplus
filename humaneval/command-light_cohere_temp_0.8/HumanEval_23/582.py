```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('') 
    Traceback (most recent call last):
      File "<string>", line 20, in strlen()
        ValueError: unexpected token '>'
    """ 
    try:
        if not string: 
            return 0
        return len(string)
    except ValueError: 
        print('Unexpected token ', end='')
        raise 
``` 
This code defines a function called `strlen` that calculates the length of a given string. The code passes tests by providing the same input and checking the output.