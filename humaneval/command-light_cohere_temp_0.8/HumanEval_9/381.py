```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [num for num in numbers if num >= 0]  # Ensure only positive numbers
    max_num = numbers[0]  # Initialize maximum number with the first element
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return [max_num]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers2 = [1, 2, 3, 0, 5]
result2 = rolling_max(numbers2)
print(result2)
```
This Python code defines a function `rolling_max` that calculates the rolling maximum element in a list of integers. The function ensures that only positive numbers are considered, initializes the maximum with the first element, and iterates through the rest of the list to find the rolling maximum element. The code then demonstrates the same concept by providing two example lists of numbers and their respective rolling maximum results.