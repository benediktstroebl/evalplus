```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+1 if i<len(numbers) else i for i in numbers] + [delimiter] * (len(numbers)-1) + [delimiter] * numbers
numbers = [1,2,3]
print(intersperse(numbers, 4))
```