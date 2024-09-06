Here's the function along with test cases:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test cases
test_cases = [
    ['abc', 'bcd', 'cde', 'array', 'a'],
    ['a b e', 'cde'],
    ['abc', 'baz'],
    ['hello world', 'xx']
]

for case in test_cases:
    actual = filter_by_prefix(case, 'a')
    assert actual == ['abc', 'array'], f"Incorrect filtering: {actual}, should be {[abc, array]}"

print("All tests passed!")
```

Please feel free to use this script and the test cases to verify the correctness of your function.