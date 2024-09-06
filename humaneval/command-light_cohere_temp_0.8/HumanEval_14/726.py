```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [x for x in string if x != '' and x != '']
test_data = {
    'abc': ['a', 'ab', 'abc'],
    'hello world': ['h', 'ello', 'world'],
    '': []  # empty string
}

for test_case, expected_result in test_data.assert test_prefixes(**test_case):
    print(f"Test case: {test_case}")
    print(f"Expected result: {expected_result}")
    print(f"Actual result: {[{test_case}]}")
```