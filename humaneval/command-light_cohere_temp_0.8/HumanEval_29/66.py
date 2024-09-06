```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test case using markdown code block
test_strings = ["abc", "bcd", "cde", "array", "more", "hello"]
test_prefix = "ac"

result = filter_by_prefix(test_strings, test_prefix)
assert result == ["abc", "array"], "Filtered strings start with 'ac'"
``` 
The code defines a function **filter_by_prefix** that filters an input list of strings based on a given prefix. The function iterates through each string in the list that starts with the provided prefix, returning them as the result. The function is designed to handle both single and multiple string inputs, and it uses the **startswith** method from Python strings to perform the filtering. The test case is included to ensure the correctness of the function's behavior.