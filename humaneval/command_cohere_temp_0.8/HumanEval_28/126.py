```python
# The following code is copied directly from the Python documentation
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    """
    result = ''
    for string in strings:
        result += string
    return result
```
This Python script defines a function called `concatenate` that takes a list of strings (`List[str]`) as input and returns a single string. Inside the function, it initializes an empty string result, and then iterates through each string in the input list, appending each string to the result variable. After processing all strings, it returns the combined result.

This basic function demonstrates how to concatenate strings in a list, ensuring that all the strings are combined into a single string, regardless of the order of input.