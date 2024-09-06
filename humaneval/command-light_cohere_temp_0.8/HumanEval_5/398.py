```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [1, 2, 3, 4]
test_delimiter = 4
test_expected = [1, 5, 7, 9]

print(f"Test results: { + test_expected })
```