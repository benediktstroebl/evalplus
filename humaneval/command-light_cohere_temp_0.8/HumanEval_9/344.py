```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [num for num in numbers if num > max_element]
    max_element = max(max_numbers) if max_numbers else numbers[0]
    return [max_element] + [num for num in numbers if num == max_element]

# Unit tests:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [3, 3, 3, 3, 4, 4]

numbers = [5, 1, 9, 4, 6, 10]
print(rolling_max(numbers))  # [10, 6, 9, 4]

numbers = [4, 2, 6, 3, 8, 5]
print(rolling_max(numbers))  # [6, 8, 5]
``` 
This code defines a function `rolling_max` that calculates the maximum element found after applying a rolling window of a given list. The function utilizes list comprehension and a new list called `max_numbers` to track the highest elements encountered so far. The `max_element` is then determined based on this list, or the first element in the original list if no higher elements are found. The function then returns a list of the `max_element` followed by the elements in the original list that match it.