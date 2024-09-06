```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers) - 1):
        if i % 2 == 0:
            result.append(numbers[i]+delimeter)
        else:
            result.append(numbers[i])
    return result

# Test cases for function
test_intersperse = [
    [], 4,
    [1, 2, 3], 4,
    [10, 20, 30], 4,
    [100, 200, 300]
]

for item in test_intersperse:
    actual = interceptsper(item)
    assert actual == item
```