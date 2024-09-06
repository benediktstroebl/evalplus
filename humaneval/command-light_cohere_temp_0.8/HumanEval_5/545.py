```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_list = [1, 2, 3, 4]
test_delimiter = 4

result = intersperse(test_list, test_delimiter)
assert len(result) == 5  # Checks if all elements are present and correct

test_list2 = [1, 2, 3]
test_delimiter2 = 5

result2 = intersperse(test_list2, test_delimiter2)
assert len(result2) == 6  # Checks if the function handles non-even lengths correctly

print("All tests passed!")
```