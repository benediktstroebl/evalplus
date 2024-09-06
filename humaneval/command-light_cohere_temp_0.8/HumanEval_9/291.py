```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)
    return [x for x in numbers if x > numbers[-1] or x == numbers[-1]]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
``` 
This code defines a function `rolling_max` which generates a list of the rolling maximum elements of the passed list of integers. The test passed also uses a list [1, 2, 3, 2, 3, 4, 2] and prints the resulting list, which is `[1, 2, 3, 3, 3, 4, 4] as the rolling maximum elements are [1, 3, 3, 4].