```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): List of strings to be concatenated

    Returns:
        str: Concatenated string
    """

    # Use the join() method to concatenate all strings in the list
    # The join() method concatenates all the items in the list into a single string
    # The string on which the join() method is called will be placed in between each pair of consecutive items from the list
    # Since we want to concatenate the strings without any separator, we call the join() method on an empty string
    concatenated_string = ''.join(strings)

    return concatenated_string

# Test the function
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines a function `concatenate` that takes a list of strings and returns a single string that is the concatenation of all the strings in the list. The join() method is used to concatenate the strings. The script also includes test cases to demonstrate the function's behavior.