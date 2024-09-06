```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python code defines a function called **filter_by_substring** that takes a list of strings and a substring as input, and returns a new list containing only the elements of the input list that contain the given substring. The code uses the array-like syntax to define the function, and the function is designed to be self-contained, as it only performs a filtering operation on the input strings and does not rely on any external variables or functions.

The code uses the **typing** module to help with type hints and better code readability. The function utilizes the language built-ins for the **find** method of the string module, which allows it to efficiently filter the strings based on whether they contain the given substring.