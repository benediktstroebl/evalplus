```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test cases
test_case_1 = ['abc', 'bcd', 'cde', 'array', 'item']
test_case_2 = ['a'b'cd', 'a'cde', 'apple', 'array']
test_case_3 = ['_abc123', '123', 'abc', '456']

print(filter_by_prefix(test_case_1, 'a'))
print(filter_by_prefix(test_case_2, 'a'))
print(filter_by_prefix(test_case_3, 'a'))
``` 
This code defines a function called `filter_by_prefix` that takes in a list of strings and a prefix, then it returns a new list that contains only the elements from the original list that match the provided prefix. 
The code then provides three test cases to verify the functionality of the `filter_by_prefix` function, which should correctly filter out the strings with the prefix 'a'.