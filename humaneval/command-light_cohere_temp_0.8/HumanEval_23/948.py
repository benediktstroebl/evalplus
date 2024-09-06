```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

#Test case 1:
assertEqual(strlen(''), 0)

#Test case 2:
assertEqual(strlen('abc'), 3)
```
This script defines a function `strlen` which calculates the length of a given string. It then passes the value 'abc' to the `strlen` function and checks if the length is indeed 3.  The code is self-contained, meaning it can be executed as a standalone Python script without requiring any external modules or functions.