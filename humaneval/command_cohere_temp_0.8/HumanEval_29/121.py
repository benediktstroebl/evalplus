```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that start with the input prefix. The syntax is using list comprehension with a filter condition. 

To test this function, you can use the following code:
```python
# Test 1: Empty list, empty prefix
test1 = filter_by_prefix([], '')
assert test1 == []

# Test 2: List with matched and unmatched strings, generic prefix
test2 = filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
assert test2 == ['abc', 'array']

# Test 3: List with matched strings, exact prefix
test3 = filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'abc')
assert test3 == ['abc']
```

This tests the function with empty input, generic and exact prefixes, both with and without matches. The `assert` statements will cause the test to fail if the actual output does not match the expected output.