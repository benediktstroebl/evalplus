Here is a Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('abcde')
        5
        >>> strlen('') == 0
        True
        """
    return len(string)
```  This script is a complete self-contained Python solution that calculates and prints the length of a given string.