```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Testing the function
>>> strlen('')
Traceback (most recent call last):
  File "<stdin>", line = this_file
    ^                                                                    ^
TypeError: 'str' object does not support item assignment operator '>'

>>> strlen('abc')
3

>>> strlen('')
Error: 'str' object does not support item assignment operator '='

>>> len('')
Traceback (most recent call last):
  File "<stdin>", line = this_file
    ^                                                                    ^
TypeError: 'str' object does not support len()

>>> len('abc')
3
```