```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Print results
print("Filtered strings:", result)
```
This code defines a function `filter_by_substring` that filters an input list of strings based on whether the `substring` is present in each string. The function uses a list comprehension with a lambda function to achieve this. 

The function is then tested using a test case that includes a list of strings and a specific `substring`. The function returns the list of strings that contain the `substring`. Finally, the code prints the filtered strings.