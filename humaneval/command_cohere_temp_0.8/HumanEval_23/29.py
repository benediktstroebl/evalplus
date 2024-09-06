```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script provides a function called `strlen` that takes a string as an argument and returns the length of the string. It utilizes the built-in `len` function to calculate the number of characters in the given string. 
The function is designed to follow the Python docstring conventions, where the double-quoted string is used to create a docstring, which serves as documentation for the strlen function, providing a clear and concise description of what the function does and how to use it. 
To run the function, simply call it with a string argument, and it will return the length of the string. For example, if you call strlen('test'), it will return the value 4, which is the length of the string 'test'. 
This approach guarantees a straightforward and efficient way to find the length of any given string, as the built-in `len` function has been meticulously optimized by the Python developers. 
It's important to note that this function does not perform any validation on the input other than checking if it can be converted to a string. If you need to handle edge cases or invalid inputs, you may need to add additional logic to the function. 
The overall solution is concise and easy to understand, providing a straightforward way to calculate the length of a string in Python.