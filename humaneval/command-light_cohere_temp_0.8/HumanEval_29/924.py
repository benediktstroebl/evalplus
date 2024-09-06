```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests
test_filter_by_prefix = []
test_filter_by_prefix.push_one('a')
test_filter_by_prefix.push_one('bc')
test_filter_by_prefix.push_one('cde')
test_filter_by_prefix.push_one('array')

def test():
    assert filter_by_prefix(test_strings, 'a') == ['a']
    assert filter_by_prefix(test_strings, 'bc') == ['bc']
    assert filter_by_prefix(test_strings, 'cde') == ['cde']

# Main function and usage
strings = ['abc', 'bcd', 'cde', 'array']
print(filter_by_prefix(strings, 'a'))
``` 
This code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The `test` function is used to verify the correctness of the `filter_by_prefix` function. 

The main code then creates a list of strings, passes it to `filter_by_prefix`, and prints the resulting list, which should contain only the strings that start with the given prefix.