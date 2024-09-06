```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
             ...
            File "<string>", line 33, in strlen()
        File "<string>", line 9, in <module>
            __line_cache__ freight error: TypeError: 'str' object does not support item assignment 
             at index: 0
    """
    return len(string)
```