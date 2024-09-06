```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Unit tests
test_case_empty = []
test_case_one_word = ['a']
test_case_multiple_words = ['abc', 'bcd', 'cde', 'array']

assert filter_by_prefix(test_case_empty, 'a') == []
assert filter_by_prefix(test_case_one_word, 'a') == ['a']
assert filter_by_prefix(test_case_multiple_words, 'a') == ['abc', 'array']

test_case_prefix_only = ['css-editor']
test_case_prefix_and_rest = ['a', 'python-ide']

assert filter_by_prefix(test_case_prefix_only, 'css') == ['css-editor']
assert filter_by_prefix(test_case_prefix_and_rest, 'python') == ['python-ide']
``` 
This Python code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the particular test cases, with various inputs, and asserts the function's expected behavior using `assert`. The code provides clear and concise assertions to validate its functionality, demonstrating its correctness and adherence to the problem's specification.