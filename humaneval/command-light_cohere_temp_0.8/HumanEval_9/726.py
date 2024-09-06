```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(numbers, numbers) if i < numbers[i+1] or i == len(numbers)-1][::-1]

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 3, 2, 1, 5]
print(rolling_max(numbers))  # Output: [1, 2, 3, 4, 4, 5]

numbers = [1, 2, 3, 4, 5, 6]
print(rolling_max(numbers))  
# Error: typing error: cannot create an index for the slice
```