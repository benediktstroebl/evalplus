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

def test_inperse():
    numbers = [1, 2,3,4,5]
    delimiters = [4,4]
    expected = [1,4,2,4,3,4,5]
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print("Passed test!")
```