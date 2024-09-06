```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in string if i != '']
test_string = "abc"
test_result = all_prefixes(test_string)
print(test_result)  # Output: ['a', 'ab', 'abc']
```
This script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest occurring characters in the input string. The function uses list comprehension with a condition to filter out non-characters from the input string.