```python
# Importing the necessary module
from typing import List


# Defining a function to concatenate a list of strings into a single string
def concatenate(strings: List[str]) -> str:
    result = ''
    for string in strings:
        result += string
    return result
```

This function takes as input a list of strings and returns a single string concatenated from the inputs in the list. It is also annotated with type hints to indicate that the input parameter should be a list of strings and the output is a string.