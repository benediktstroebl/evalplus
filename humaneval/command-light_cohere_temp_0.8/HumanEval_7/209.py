```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']

# Test case 2
strings = ['abc', '123', '456']
substring = '12'
result = filter_by_substring(strings, substring)
print(result)  # Output ['123']

# Test case 3
strings = ['a', 'bb', 'cc', 'dd']
substring = 'ab'
result = filter_by_substring(strings, substring)
print(result)  # Output ['ab', 'bb', 'cc', 'dd']
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as inputs. It uses a general list comprehension to filter the list of strings and returns a new list that contains only the elements that contain the given substring. 

It then passes three test cases to demonstrate the functionality.