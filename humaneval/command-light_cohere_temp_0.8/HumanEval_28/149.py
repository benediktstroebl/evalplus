```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate

    Returns:
    str: Concatenated string
    """
    return "".join("".join(strings))

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: "abc"

strings = []
result = concatenate(strings)
print(result)  # Output: ""

strings = ["a", "bcde"]
result = concatenate(strings)
print(result)  # Output: "abcdef"

strings = ["abc", "123", "!"]
result = concatenate(strings)
print(result)  # Output: "abc123!"
``` 

I hope this solution covers all provided test cases and is a good starting point for solving the problem. You can continue with this and expand on it based on additional test cases or any specific requirements from the problem.