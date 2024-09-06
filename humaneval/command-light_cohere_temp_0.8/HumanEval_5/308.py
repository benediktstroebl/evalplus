```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[:-1] + [delimiter] + numbers[-1:]

# Test the function with sample inputs/outputs
numbers = [1, 2, 3, 4, 5]
delimiter = 4

expected = [1, 4, 2, 4, 3, 5]
result = intersperse(numbers, delimiter)

if expected == result:
    print("The function works as expected.")
else:
    print("The function did not work as expected.")
```