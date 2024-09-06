```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+delimiter for num, delimiter in zip(numbers, delimeter)]
# Test the function
numbers = [1, 2, 3]
delimiters = [4,4,12]
result = intersperse(numbers, delimiters)
print(result)  # expected output: [1, 4, 12, 2, 12, 3]
```