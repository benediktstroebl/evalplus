```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that include the `substring` to the new list.

This solution should address the problem statement and help you filter a list of strings based on a substring they contain. Let me know if you would like me to explain any part of the code in more detail, or provide further examples. 

For practical applications, if you plan to use this function in a larger program, consider adding documentation and comments to make it more understandable for yourself and others who might use or read your code.