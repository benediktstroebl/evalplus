```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            File "<ipythonfile>", line 10, in strlen
            File "<string>", line 8, in function '__main__':
                ...
            File "<ipythonfile>", line 1, in strlen
                File "<string>", line 6, in <module>.strlen cirular_func:7>
                File "<ipythonfile>", line 14, in strlen
        File "<ipythonfile>", line 1, in __main__
        GlobalError: 'object' object has no attribute '__dict__'
    """
    return len(string)
```