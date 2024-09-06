```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() for char in string)
```
This script provides a function that takes a string as an argument and returns a new string with the letters flipped from their original case. For example, the input **'Hello'** would return **'hELLO'**. This behavior is prompted by the **'.swapcase()'** method that is applied to each character in the string.