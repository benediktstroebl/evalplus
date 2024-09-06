```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "hello world", "here is a sample string", "more strings please"]
substring = "a"

print("Test case 1 result:", filter_by_substring(strings, substring))
print("-----------------------")

strings = ["abc", "hello world", "here is a sample string", "is"]
substring = "hello"

print("Test case 2 result:", filter_by_substring(strings, substring))
```
This code defines a function called `filter_by_substring`, which takes two arguments: a list of strings and a substring. The function uses a string technique to find all instances of the substring in the input list and returns the filtered list.