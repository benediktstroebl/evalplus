```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)
   max = numbers[-1] 
    return [max for x in numbers if x > max] + [max]

# sample test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
test_rolling_max = [rolling_max(numbers)][::-1]
print(test_rolling_max)
```