```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Run the function with the same input as described in the problem statement
test_strings = ['abc', 'bcd', 'cde', 'array', 'test']
test_prefix = 'a'
result = filter_by_prefix(test_strings, test_prefix)
assert result == ['abc', 'array', 'test']

# Run the function with a custom input list and a specific prefix
input_strings = ['abc', 'bcd', 'cde', 'd']
input_prefix = 'cd'
result = filter_by_prefix(input_strings, input_prefix)
assert result == ['cd']

print('Passed all tests')
``` 
This Python script provides a self-contained function `filter_by_prefix` that filters a list of strings based on a given prefix. The function uses the method `startswith` to check if each string in the list starts with the given prefix. 

The function then returns a new list containing only the strings from the original list that match the given prefix.