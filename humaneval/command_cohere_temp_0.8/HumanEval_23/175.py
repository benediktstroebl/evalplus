```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script defines a function called `strlen` that takes a string as an argument and returns the length of that string. The function uses the `len()` function, which is a built-in Python function, to calculate the number of characters in the given string. 

This behaves as intended for empty strings and strings of different lengths.
```python
>>> strlen("")
0
>>> strlen("abc")
3
>>> strlen("abcd")
4
``` 
You can easily incorporate this solution into your collection of Python tools, as it provides a clean and reusable way to determine the length of any given string.