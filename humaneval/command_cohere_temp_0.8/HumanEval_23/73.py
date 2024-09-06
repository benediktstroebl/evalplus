```python
def strlen(string: str) -> int:
    """ Returns the length of the given string """
    return len(string)
```
This Python script provides a function termed `strlen` that takes a string argument and returns an integer representing the length of the string. The function utilizes the `len()` function, a built-in Python function that provides the length of a given sequence, in this case, the given string. 

This function is designed with a docstring, which is a multi-line string that documents the purpose and usage of the function. The docstring consists of a summary line describing the function's purpose, followed by a line of `>>>` markers. These markers denote the expected format of the function's input and the format of its output, thereby assisting users in understanding how to employ the function properly. 

To execute this function, you can call it in your Python environment with an input string, and it will return the length of the provided string. 

An example of this function run is: 
```python
print(strlen('Hello, world!'))
```
This will output: 
```
13
```