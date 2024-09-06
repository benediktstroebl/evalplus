```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # sort the list in ascending order
    numbers.sort(numbers)
    # get the two elements that are the smallest and largest numbers in the sorted list
    elements = numbers[0:min(len(numbers), 2)] + numbers[-1:max(len(numbers), 2)]
    return (min(elements), max(elements))
```
The function sorts the input list of numbers in ascending order, then uses the list slicing techniques to select the first and last two elements from the sorted list, which are the smallest and largest numbers. Then, the function returns the minimum and maximum elements to return the closest pair of numbers.