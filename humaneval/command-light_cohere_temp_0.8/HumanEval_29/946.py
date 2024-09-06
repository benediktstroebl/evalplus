```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings for those starting with a given prefix."""
    return [string for string in strings if string[0] == prefix]

# Test cases
strings = ["abc", "bcd", "cde", "a", "array", "hello"]
prefix = "a"

result = filter_by_prefix(strings, prefix)
print("Filter results:", result)

if len(result) == 3:
    print("Passed test!")
else:
    print("Failed test.")
```
The provided code snippet has a function called `filter_by_prefix`, which takes two parameters: a list of strings and a prefix. By utilizing a filter notation, it creates a new list that contains elements from the input strings that match the given prefix. 

The test cases follow: There's an input list of strings and a target prefix. Then, the `filter_by_prefix` function is called with these parameters, and the results are stored in the `result` variable. The code then checks if the length of `result` is 3, which indicates that the test passed. If so, it prints "Passed test!". Otherwise, it prints "Failed test."