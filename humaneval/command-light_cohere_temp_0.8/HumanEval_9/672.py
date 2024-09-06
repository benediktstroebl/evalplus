```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted((num for num in numbers if num >= numbers[-1]), reverse=True)]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [1, 2, 3, 3, 3, 4, 4]
```
This Python function, named `rolling_max`, takes a list of integers as an argument and returns a new list containing the rolling maximum elements found in the input sequence. 

The `sorted` function is used to generate a sorted list of integers, and a generator expression `(num for num in numbers if num >= numbers[-1])` is used to select the elements greater than the last element in the sorted sequence. 

The `reverse=True` argument is used to reverse the order of elements, ensuring that the maximum element is at the beginning of the sequence.

The function then returns the reversed sorted list, which contains the rolling maximum elements found in the input sequence.