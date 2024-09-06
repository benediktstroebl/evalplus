```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "xx", " abcdef"]
prefix = "a"

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
``` 
This code defines a function called **filter_by_prefix** that filters an input list of strings based on a given prefix. The function uses the process of iterating through the input strings and checking if each string starts with the provided prefix. It returns a the filtered list that contains only those strings that match the condition.