```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with sample inputs and expected outputs
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call and print results
print(filter_by_substring(strings, substring))
```
This Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. The function iterates through each character in the list to check if the given substring exists in it. 

The function is then tested with a sample input and the output is printed.