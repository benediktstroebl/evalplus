```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n,i in zip(sorted(numbers),range(len(numbers)))]
# Test cases
numbers = [1,2,3,2,3,4,2]
result = rolling_max(numbers)
print(result)
result = rolling_max([4,1,2])
print(result)
result = rolling_max([-5,6,7])
print(result)
result = rolling_max([1,1,1])
print(result)
```