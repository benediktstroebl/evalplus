```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(x) for x in numbers.
    return ''.join(sorted(numbers))

#Test cases
test_cases = [
    "three one five",
    "zero two three",
    "one two three four",
    "two three six seven",
    "six seven eight nine"
]

for test in test_cases:
    result = sort_numbers(test)
    assert result == ''.join(sorted(test))
```