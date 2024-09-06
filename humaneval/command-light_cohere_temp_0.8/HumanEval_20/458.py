```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements that are the closest to each other.
   
    numbers = sorted(numbers, reverse=True)
    closest1 = next((num for num in numbers if num < numbers[0]), default=float('inf'))
    closest2 = next((num for num in numbers if num > numbers[-1]), default=float('inf'))
    return closest1, closest2
```

This function utilizes the next() function to select the first and last elements in the list, then checks if the current element is less than the first element, if true, then it's the closest1, else it's the closest2. The same closest elements in the list are returned in order, with the smallest element as the first element and the larger element as the second element.