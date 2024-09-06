```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements in an ascending list of integers.
    Each element in the max list will be the maximum value of elements in the list up to the current index
    """
    return [n for n in numbers if n == numbers[-1]] + [n for n in numbers][1:]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)

numbers = [5,1,2,3,4,3]
result = rolling_max(numbers)
print(result)

numbers = [1, , , 10, , ,100]
result = rolling_max(numbers)
print(result)
```
The code defines a function called rolling_max that takes a list of integers as input and generates a new list that contains the maximum element from the input list at each index. The output of the maximum element found over the entire sequence is then printed out.