```python
def strlen(string: str) -> int:
    """ Return length of given string
    Returns length of string
    """
    return len(string)

# Testing the function
>>> strlen('')
==> 0

>>> strlen('abc')
==> 3

>>> strlen('123')
==> 3

# Wrong input -- should raise an error!
>>> strlen('')
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    ^
SyntaxError: invalid literal for int() with base '+' 
```