```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join("".join(strings))

# Test cases
test_cases = [
    [],
    ['a', 'b', 'c'],
    ['a',],
    ['a', 'bc', ''],
    ['abc'],
    ['a', 'b', 'ccc'],
]

for test_case in test_cases:
    actual_result = concatenate(test_case)
    print(f"Expected: '{test_case}\nActual: {actual_result}"
        )
```