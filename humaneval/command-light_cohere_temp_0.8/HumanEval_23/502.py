```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('') 
        Traceback (most recent call last):
           File "<string_module>'
              ... <line 1>...</string_module>
                ^
          File "<string_module>'
    File "<string_module>.__pyi_ord">128
    UnicodeDecodeError: weird continuation
    """
    return len(string)
```