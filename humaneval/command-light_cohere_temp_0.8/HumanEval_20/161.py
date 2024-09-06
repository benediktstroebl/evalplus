```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Similar to QuickSelect, the approach here is to find the element with the smallest index in the sorted numbers array.
    # Then sort the reluatively to ensure that you have numbers ordered smallest to largest, then find the smallest one, and use that as a pivot.
    `numbers = sorted(numbers)
    smallest_element = numbers[0]
    for current_element in numbers[1:]:
        if current_element < smallest_element:
            smallest_element = current_element
    return smallest_element, numbers[1]
```
This script defines a function, `find_closest_elements`, that takes a list of numbers as an argument and returns a tuple of the closest elements in the list. The function sorts the numbers list by float and then loops through the sorted numbers, keeping track of the smallest element seen so far. It then compares each element in the list to the current smallest element seen so far, and if the current element is smaller than the current smallest element, it becomes the new smallest element. The function returns this smallest element, and the corresponding number, from the list.