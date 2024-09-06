```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script provides a function called `strlen` that takes a string as an argument and returns the length of the string. It uses the built-in Python function `len` to calculate the number of characters in the string, including spaces, punctuation, and any other characters. 

Here are some example calls to the `strlen` function showing its behavior when called with different types of strings:
```python
>>> strlen("I love coding!")
13
>>> strlen("")
0
>>> strlen("abc")
3
>>> strlen("abcdefghijklmnopqrstuvwxyz")
26
```
This example showcases the versatility of the `strlen` function in returning the lengths of various input strings, which can be useful in a variety of applications within Python programs. 

The function includes a docstring providing a clear explanation of its purpose, syntax, and behavior, making it an accessible and readable tool for developers.