```python
# Importing the required module
from typing import List

# Defining the concatenate function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Empty lists result in an empty string.
    """
    result = ''.join(strings)
    return result
```

This Python script defines a function called `concatenate` that takes a list of strings as input and returns a single string that concatenates all the input strings. The function is designed to handle empty lists gracefully, as demonstrated in the provided test cases.