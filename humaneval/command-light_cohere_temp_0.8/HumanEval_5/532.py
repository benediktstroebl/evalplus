```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]+delimeter)
        else:
            result.append(numbers[i])
    return result

# Test cases
test_data = [4, 2,3]
test_result = intersperse(test_data, 4)
print(test_result)  # Expected Output: [1,4,2,4,3]
test_data2 = [1,2,3,4]
test_result2 = intersperse(test_data2, 4)
print(test_result2)  # Expected Output: [1,4,2,4]
```