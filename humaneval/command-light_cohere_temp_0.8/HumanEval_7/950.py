```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.contains(substring)]
 simple_filter-like functionality. 

list1 = ['abc', 'abcd', 'cde', '5le', 'a']
list2 = ['a', 'b', 'cd', 'ad', 's', 'as']
print(filter_by_substring(list1, 'a'))
print(filter_by_substring(list2, 'ad'))
```