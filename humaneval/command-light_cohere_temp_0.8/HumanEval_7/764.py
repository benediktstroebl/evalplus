```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Example usage
strings = ["abc", "bacd", "cde", "array"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # ['abc', 'bacd', 'array']
```
This function efficiently filters a list of strings and returns only the ones that contain the specified substring. It utilizes a simple and effective list comprehension to achieve this, making the code concise and readable.