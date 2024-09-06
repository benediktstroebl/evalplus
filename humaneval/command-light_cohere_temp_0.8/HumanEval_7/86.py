```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test Case 1
strings = ["abc", "bacd", "cde", "array"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  
# Expected Output ['abc', 'bacd', 'array']
```

The code defines a function `filter_by_substring` that takes a list of strings and a substring as input. It then uses a filtering to create a new list that contains only the strings that contain the given substring, the output is then printed.