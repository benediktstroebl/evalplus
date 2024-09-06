```python
# Import the necessary module
from typing import List


# Define the function
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    result = ''
    for string in strings:
        result += string
    return result


# Provide example tests
>>> concatenate([])
''

>>> concatenate(['a', 'b', 'c'])
'abc'
```

The `concatenate` function takes a list of strings (`List[str]`) as an argument and returns a single string that consists of the concatenated strings in the list. It uses a for loop to iterate over each string in the list and appends them to a result string, which is initially set to an empty string. The function returns the `result` string after all strings have been concatenated.  The example tests demonstrate its functionality when an empty list and a list with three strings are provided.  This solution is efficient and has a time complexity of `O(n)` since it iterates through the list once, resulting in a single concatenated string.