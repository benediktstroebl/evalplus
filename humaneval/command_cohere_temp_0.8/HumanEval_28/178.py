```python
# Import the necessary module
from typing import List

# Define the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # If the input list is empty, return an empty string
    if not strings:
        return ''

    # Use concatenation to combine the strings in the list and return the result
    return ''.join(strings)

# Example usage
test_list = ['a', 'b', 'c']
result = concatenate(test_list)

# Print the result
print(result)  # 'abc'
```

This code provides a function called `concatenate` that takes a list of strings as input and returns a single string as output, which is the concatenation of all the strings in the list. The function checks if the input list is empty, and if so, it returns an empty string. Otherwise, it uses the `join` method to concatenate the strings in the list. The example usage demonstrates how to call the function with a sample list of strings and print the resulting concatenated string.