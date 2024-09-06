Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_windows: int) -> List[int]:
    return [max(list(zip(*[iter(numbers)]*rolling_windows)))) for i in range(len(numbers)-rolling_windows+1)]
```

The provided code defines a function rolling_max that takes a list of numbers and a rolling window size as input. It creates a new list containing the maximum element from a sliding window of the specified size for each element in the input list. The result is a list where each element represents the maximum within its respective rolling window. 

To achieve this, the code utilizes a list comprehension with a generator expression inside. The generator expression max(list(zip(*[iter(numbers)]*rolling_windows))) takes each sublist of size rolling_windows from the input list numbers, zips them together, and returns the maximum element. The outer list comprehension iterates over the entire input list, producing a new list where each element is the maximum value within its rolling window.

Note that the function rolling_max assumes the input list contains at least `rolling_windows` numbers to operate on. If the input list is insufficiently long, the function will raise a ValueError. Additionally, the function is not optimized for large lists, as it iterates through the entire list multiple times. It may be suitable for smaller lists or cases where efficiency is not a primary concern.