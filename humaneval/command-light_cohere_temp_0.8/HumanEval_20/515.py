```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two closest numbers in the list, and returns them in order (smaller number, larger number)
    """
    numbers = [num for num in numbers if num != float('inf')]
    numbers.sort(sorted(key=lambda x: x, reverse=True))
    closest1 = min(numbers, key=lambda x: x)
    closest2 = max(numbers, key=lambda x: x)
    return closest1, closest2
```
This code defines a function called **find_closest_elements** that takes in a list of floating-point numbers as input and returns a tuple containing the two closest numbers in order. The function first filters out the previous cases and sorts the numbers based on their value in descending order. It then finds the the smallest number and the largest number in the sorted list and returns them in the tuple.