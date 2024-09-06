```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('')
        Traceback (most recent call last):
            File "<filename>", line 6, in strlen
            raise ValueError('Input string is empty')
        File "<ipythoninput>.py", line 4, in function '__main__':
            strlen('')
        File "<ipythoninput>.pyi', line 3, in __main__'
        ValueError: Input string is empty
    """
    if not string:
        raise ValueError("Input string is empty")
    return len(string)

def __main__():
    string = "abc"
    print(strlen(string))

__main__()
```