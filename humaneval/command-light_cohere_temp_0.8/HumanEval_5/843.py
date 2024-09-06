```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+delimiter for num, delimiter in zip(numbers, delimeter)]
# Test case:
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]
print(f"Result: {expected}")
 ```