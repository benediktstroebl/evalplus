```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This function uses the built-in `len()` function to calculate the number of characters in the given string. It works for any string, including empty strings, and returns an integer value. 
The tests would look like this:
```python
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('abcdefghijklmnopqrstuvwxyz')
26
``` 
The function returns the appropriate length for any string input.