```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)  # Sort the list of numbers.
    ys = [max(numbers)
    while ys[-1] == numbers[0]:
        numbers.pop(0)
        ys.insert(0, numbers[0])
        numbers.append(numbers.pop(0))
    max_element = ys[-1]
    numbers.remove(max_element)
    return numbers
``` 
This function takes a list of integers as input and returns a new list with the maximum element from the original list. It uses the insertion and pop methods to simulate rolling the maximum element up in the list.