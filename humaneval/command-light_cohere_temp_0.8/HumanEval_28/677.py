Sure, here's a self-contained Python script that defines a function `concatenate` solving the problem you provided:

```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Returns: str - Concatenated string
    """
    return ''.join(strings)
# Test case 1
strings = [""]
result = concatenate(strings)
assert result == "", "Error: Expected empty string, got %s" % result

# Test case 2
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc", "Error: Expected 'abc', got %s" % result

# Test case 3
strings = ["a"]
result = concatenate(strings)
assert result == "a", "Error: Expected 'a', got %s" % result
```

Please feel free to use this script and ask any follow-up questions or additional requests.