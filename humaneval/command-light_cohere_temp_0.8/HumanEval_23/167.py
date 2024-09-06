Here is a self-contained Python script that defines a function strlen that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('ab')
        2
        >>> strlen('') == 0
        True
        """
    if not string:  # empty string
        return 0
    return len(string)
```  This code provides a function that calculates and returns the length of a given string, passing all the test cases.