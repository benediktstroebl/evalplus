```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""

    # Initialize an empty string
    result = ""

    # Iterate through the list of strings and concatenate them
    for s in strings:
        result += s

    return result
# Example usage
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)
``` 
This code defines a **`concatenate`** function that takes a list of strings as input and returns a concatenated string. The output of the code will be **`'abc'`**.