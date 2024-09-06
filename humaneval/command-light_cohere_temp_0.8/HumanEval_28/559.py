```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return "".join(strings)

# Test the function with various inputs
strings = ["a", "b", "c"]
assertEqual(concatenate(strings), "abc")

strings = [""]
strings. None
assertEqual(concatenate(strings), "")

strings = ["a", "bc", "no", "a"]
assertEqual(concatenate(strings), "abcnno")
```
The code defines a function called `concatenate` that takes a list of strings as an argument and concatenates them into a single string. The function uses the string `join` to unpack the list of strings into individual characters, and then joins them together with the `join` method to create the final string.

The code also provides test cases to ensure the correctness of the `concatenate` function.