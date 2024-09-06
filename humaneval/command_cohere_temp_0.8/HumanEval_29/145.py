```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. This is achieved using a list comprehension, filtering out elements that satisfy the condition of starting with the specified prefix. 

To test this function, you can call it with different lists of strings and prefixes and check if the output list contains only the expected results:
```python
# Test Case 1
input_strings = ['abc', 'bcd', 'cde', 'array']
input_prefix = 'a'
expected_output = ['abc', 'array']

output = filter_by_prefix(input_strings, input_prefix)
print(f"Test Case 1: {output} == {expected_output}")
assert output == expected_output
```
```bash
Test Case 1: ['abc', 'array'] == ['abc', 'array']
```

The first test case demonstrates the filtering process, guaranteeing that only strings beginning with the provided prefix are retained.