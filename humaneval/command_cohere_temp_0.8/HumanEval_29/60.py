```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create a new list by applying an operation to each item in the existing list. 

To use the `filter_by_prefix` function, you can simply call it with your list of strings and the desired prefix as shown below:
```python
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```

This will filter the `strings` list and return a new list containing only the strings that start with the prefix 'a'. 

To validate the functionality of the function, you can also use the following test cases:
```python
# Test case 1
empty_list = []
empty_prefix = 'a'
test_result = filter_by_prefix(empty_list, empty_prefix)
assert test_result == []

# Test case 2
list_with_prefix = ['abc', 'bcd', 'cde', 'array']
prefix_to_match = 'a'
test_result = filter_by_prefix(list_with_prefix, prefix_to_match)
assert test_result == ['abc', 'array']

# Test case 3
list_with_multiple_prefixes = ['apple', 'appetizer', 'append', 'applepie']
prefix_to_match = 'app'
test_result = filter_by_prefix(list_with_multiple_prefixes, prefix_to_match)
assert test_result == ['apple', 'appetizer', 'append']
```