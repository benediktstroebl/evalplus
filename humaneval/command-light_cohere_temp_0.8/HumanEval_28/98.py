```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)

# Test case 1
test_case_1 = [
    "hello",
    "world", 
    "hello"
]
print(concatenate(test_case_1)) # Output: "hworldol"

# Test case 2
test_case_2 = ["a", "b", "c"]
print(concatenate(test_case_2)) # Output: "abc"

# Test case 3
test_case_3 = []
print(concatenate(test_case_3)) # Output: ""
```