```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+i*delimeter for i,num in enumerate(numbers)]
# tests:
numbers = [4,1,9,3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result == [5,8,7,6])
print(result == [1,4,10,3,9])
```