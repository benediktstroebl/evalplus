```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script defines a function named strlen that takes a string as an argument and returns the length of that string. The function utilizes the built-in Python function len to determine the number of characters in the input string. 

This fundamental function is widely used in various programming tasks, including reading text from files or consoles, manipulating strings, and validating user inputs.

If no argument is provided, or the argument is NULL, the function will return 0, which is generally considered as an error value. This is because empty strings are typically used as placeholders in Python. This function rightly returns 0 for an empty string as its definition states 'Returns the length of the given string'. 

Here's an example of how you can use this function in action:
```python
string = "Hello, World!"
length = strlen(string)
print(length)
```
This code will print out the length of the string 'Hello, World!', which is 13.