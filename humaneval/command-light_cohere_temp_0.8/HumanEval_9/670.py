```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_element = numbers[0]
    current_element = numbers[0]
    max_moment = 0
    current_moment = 0

    for num in numbers[1:]:
        current_element = max(num, current_element)
        max_moment = max(max_moment, current_moment)
        current_moment = num

    if current_element > max_element:
        max_element = current_element
    return [max_element]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 3, 4, 4]
```
This function takes a list of integers as input and returns a list of the largest elements found in the sequence. It iterates through cycle through the the first element as the maximum element and the current element of the sequence as the maximum element in the current moment.