```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases
test_case_1 = ['abc', 'bcd', 'cde', 'a', 'array', 'begin', 'ab']
test_case_2 = ['a', 'bcde', 'asddf', 'begin', 'ab']
test_case_3 = ['abcde']
test_case_4 = ['hello', 'world', '!include', 'python']

print(f'test_case_1':filter_by_prefix(test_case_1, 'a'))
print('--')
print(f'test_case_2':filter_by_prefix(test_case_2, 'a'))
print('--')
print(f'test_case_3':filter_by_prefix(test_case_3, 'a'))
print('--')
print(f'test_case_4':filter_by_prefix(test_case_4, 'include'))
``` 
This code defines a function called filter_by_prefix that takes in a list of strings and a prefix as input and returns a new list that contains only the elements from the input list that start with the prefix. The function uses the pattern matching to identify the elements with the prefix, and the function returns the resulting new list.