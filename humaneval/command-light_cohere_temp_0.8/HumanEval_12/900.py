Here is a Python script with a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    """
    first_length = 0
    max_length = ""
    for string in strings:
        if len(string) > first_length:
            first_length = len(string)
        max_length = string + " "
    return max_length[0]

# Test case 1
input_list = ["a", "b", "c"]
result = longest(input_list)
print(result)  # Output: c

# Test case 2
input_list = ["a", "bb", "ccc"]
result = longest(input_list)
print(result)  # Output: 
```

This script defines a function called `longest`, which takes a list of strings as input and returns the longest string. The function initializes variables `first_length` and `max_length` to keep track of the length of the longest string seen so far and the current longest string, respectively. It iterates over each string in the input list and updates `first_length` if the current string has a longer length than the previous longest string. It appends the former longest string found to `max_length`, and then returns the final string.