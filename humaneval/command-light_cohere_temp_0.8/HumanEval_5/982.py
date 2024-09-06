```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+delimeter for num in numbers for _ in range(2)] + numbers[-1:] 
# tests
numbers = [1,2,3]
print(invisalign(numbers, 4))  # [1,4,2,4,3]
```  This solves the problem of inserting a number 'delimiter' between every two elements in a list. The solution is a list of the concatenated numbers and the last element of the original list.