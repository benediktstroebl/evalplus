```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Test case:
numbers = [1, 2, 3]
print(inperse(numbers, 4))  # Expected Output: [1, 4, 2, 4, 3]
```