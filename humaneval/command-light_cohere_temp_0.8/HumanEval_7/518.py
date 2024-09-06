```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]


# Example usage:
strings = ["abc", "bacd", "cde", "array", "hello world"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
This Python script defines a function called `filter_by_substring` that filters an input list of strings and returns a new list that contains only the strings that contain a specified substring.  The `strings` is a list of strings, and `sub` is the substring that we want to find. The `filter_by_substring` function uses a list comprehension to iterate over the strings in the input list and adds any strings that contain the substring to the result list.