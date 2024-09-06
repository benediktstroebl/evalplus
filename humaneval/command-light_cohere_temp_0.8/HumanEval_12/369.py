```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string in the list.
    Args:
        strings (List[str]): list of strings
    Returns:
        str: length of the longest string
    """
    if not strings:
        return None
    max_len = max(len(string) for string in strings)
    return max_len
# Unit tests
strings = ["a", "bb", "ccc"]
test_longest = [ longest(strings) == len("ccc") ]
print(test_longest)  # Output: [True]
``` 
The code defines a function `longest` that takes a list of strings and returns the length of the longest string in the list. The function uses the max function to find the length of the longest string, and then returns it. 

The test cases are also created and pass the test by checking if the result of calling the `longest` function with a list of strings is equal to the length of the longest string in the list, which is "ccc".