```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    List of integers -> List of rolling max element found until given moment 
    in the sequence.
    """
   
    list comprehension to the first occurrence of max element
    """
    list_of_rolling_max = [num for num in numbers if num == numbers[-1]]
    return list_of_rolling_max

# test case 1 
numbers = [1, 2, 3, 4, 5]
rolling_max_value = rolling_max(numbers)
print("rolling_max:", rolling_max_value)  # [3, 4, 5]

# test case 2
numbers = [1, 2, 2, 3, 3, 4, 5]
rolling_max_value = rolling_max(numbers)
print("rolling_max:", rolling_max_value)  # [2, 3, 4]

# test case 3
numbers = [1, 2, 4, 2, 3, 3, 5, 6]
rolling_max_value = rolling_max(numbers)
print("rolling_max:", rolling_max_value)  # [3, 4, 5]

# test case 4
numbers = [1, 10, 2, 4, 6, 8, 10]
rolling_max_value = rolling_max(numbers)
print("rolling_max:", rolling_max_value)  # [10, 8, 10]

# test case 5
numbers = [1, 0, 0]
rolling_max_value = rolling_max(numbers)
print("rolling_max:", rolling_max_value)  # []
```