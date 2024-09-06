```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num >= 0]  # Convert list to positive numbers
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return [max_num]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
This script defines a function `rolling_max` that takes a list of integers and returns the list of the maximum elements after applying a rolling window approach. The script tests the example of using the function with a sample input list, and the output is printed to the console.