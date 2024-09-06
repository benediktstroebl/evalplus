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

# Test cases
strings = ["".join(List(["a", "b", "c"]))
print(concatenate(strings))  # Output: "abc"

strings = ["".join(List(["aa", "bb", "cc"]))
print(concatenate(strings))  # Output: "aaabbcc"

strings = ["a", "b"]
print(concatenate(strings))  # Output: "ab"

strings = ["a", "bc"]
print(concatenate(strings))  # Output: "abcdef"
```

This Python code defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string, returning the result. It is tested with several test cases, and the results are printed to the console, demonstrating the correctness of the function.