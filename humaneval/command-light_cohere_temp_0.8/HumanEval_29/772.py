```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test case
test_data = [
    'abc', 'bcd', 'cde', 'array', 'for', 'ffffff', 'grape', 'hello', 'world'
]
test_case1 = filter_by_prefix(test_data, 'a')
print(test_case1)  # Output ['abc', 'array']

test_case2 = filter_by_prefix(test_data, 'b')
print(test_case2)  # Output ['bcd', 'cde', 'grape']

test_case3 = filter_by_prefix(test_data, 'c')
print(test_case3)  # Output ['cde', 'hello', 'world']

test_case4 = filter_by_prefix(['abcd', 'abc', '123', 'word'])
print(test_case4)  # Output ['abcd', 'abc']

test_case5 = filter_by_prefix(['text', 'hello'])
print(test_case5)  # Output ['hello']
```