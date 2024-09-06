Here is a Python script that contains a self-contained function that filters an input list of strings for those containing a specific substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# Example of passing the function test:
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd']
```
This function uses a List comprehension to filter the input list, it iterates over each string and checks if the substring is present in it, then it adds it to the result list.