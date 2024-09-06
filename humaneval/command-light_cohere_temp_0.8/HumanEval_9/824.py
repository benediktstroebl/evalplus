```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers. rowing the max_num = numbers[0]
    max_num_index = numbers.indexof(max_num)
    max_new = numbers[max_num_index]
    numbers.append(max_new)
    max_num_index = max_num_index + 1
    return numbers[:max_num_index]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
``` 
This Python code defines a function called rolling_max that takes a list of integers as input and generates a new list of integers with the maximum element from the list rolling over. The sequence of elements is continuously updated with the current maximum element until the next one is encountered.