```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]+delimiter)
    else:
        result.append(numbers[i])
    return result
test_intersperse = [1,2,3]
print(intersperse(test_intersperse, 4)) # Expected output: [1,4,2,4,3]
```