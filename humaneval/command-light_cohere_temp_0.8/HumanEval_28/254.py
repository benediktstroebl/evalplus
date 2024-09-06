```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        str: concatenated string
    """
    return "".join(strings)

# Example usage
strings = ["a", "b", "c"]
print(concatenate(strings))  # Output: 'abc'

strings = []
strings. strings = ["1", "2", "3"]
print(concatenate(strings))  # Output: '123'

strings = ["a"] * 5
print(concatenate(strings))  # Output: 'aaa'

strings = List("hello", "world")
print(concatenate(strings))  # Output: 'helloworld'
```
This code defines a function called **concatenate** that takes a list of strings as an argument and returns the concatenated string by using the **join()** method. The test cases demonstrate how the can correctly concatenate the strings to form the expected output.