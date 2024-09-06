```python
def strlen(string: str) -> int:
    """ Return length of given string
    :param string: input string
    :return: length of the string
    """
    return len(string)
```
This Python script defines a function `strlen` that takes a string as an argument and returns the length of the string. The function uses the `len()` function to calculate the number of characters in the string, including spaces, special characters, and punctuation. 

The function is designed to be self-contained, meaning that it does not rely on any external variables or functions. It is a stand-alone solution for calculating the length of a string, and it can be called from anywhere in Python without any dependencies. 

Here is an example of how to use the `strlen` function:
```python
print(strlen("Test String")) # Output: 11
```
This would print the length of the string "Test String", which is 11.