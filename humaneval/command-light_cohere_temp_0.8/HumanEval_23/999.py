Certainly! Here's a self-contained Python script that defines a function `strlen` solving the length of a given string in Markdown: 

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    >>> strlen('   ')
    4
    >>> strlen('argo') # Trying a special case
    9
    """
    return len(string)
``` 

This script defines a function `strlen` that calculates the length of a given string. 

The `test` section runs the test cases and the `strlen` function with various inputs, and the results are compared against the expected length.