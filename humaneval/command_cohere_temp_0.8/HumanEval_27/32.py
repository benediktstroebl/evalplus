```python
def flip_case(string: str) -> str:
    """
    Flip case of characters in a string. Turns lowercase characters to uppercase and uppercase characters to lowercase.
    """
    return string.swapcase()
```
This function utilizes the `swapcase` method, which directly converts uppercase characters to lowercase and vice versa. This is a more efficient solution compared to manually toggling each character. The `"""` denotes a multi-line Python docstring that provides a description of the function's purpose, inputs, and behavior. 

To better illustrate its functionality, let's use the example provided in the original prompt:
```python
>>> flip_case('Hello')
'hELLO'
```
This exemplifies the kind of output you can expect from the function.