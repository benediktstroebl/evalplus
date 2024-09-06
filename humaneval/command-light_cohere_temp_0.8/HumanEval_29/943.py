```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests for filter_by_prefix function
test_filter_by_prefix = [
    ('', 'a'),  # 'a' should be returned
    ('b', 'c'),  # No match
    ('cd', 'a'),  # 'a' should be returned
    ('', 'cd'),  # Empty string should be returned
    ('array', 'a'),  # Array should be returned
    ('a', 'b', 'c'),  # Should return ['a', 'b', 'c']
]

def test_case_insensitive(test_list):
    actual_result = filter_by_prefix(test_list, 'a')
    assert actual_result == test_list

test_filter_by_prefix
test_case_insensitive(test_filter_by_prefix)
```