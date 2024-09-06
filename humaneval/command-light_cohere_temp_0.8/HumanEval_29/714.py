```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"

# Function call
result = filter_by_prefix(strings, prefix)

print(result)  # Output: ['abc', 'array']
``` 
This code defines a function called **`filter_by_prefix`** that takes a list of strings and a prefix as input. It uses the filtering with the list comprehension to filter the strings that start with the given prefix.