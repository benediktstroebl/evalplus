```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [x for x in numbers if x > 0]  # Remove non-positive numbers
    max_num = max(numbers)  # Find the maximum number
    max_index = numbers.index(max_num)  # Find the index of the maximum number
    return [max_num] + [num for num in numbers if num == max_index]  # Return the maximum number and all numbers after it in the sequence
```

This script defines a function `rolling_max` that takes a list of integers as input and returns a new list containing the maximum number from the input list and all subsequent numbers that equal to the index of the maximum. The function effectively removes non-positive numbers from the input and handles the case where the list contains only one element.  This's an example usage of the function, we can pass a list of numbers and obtain the desired result.