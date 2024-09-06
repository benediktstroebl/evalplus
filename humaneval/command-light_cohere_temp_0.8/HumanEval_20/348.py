```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # sort the list based on numbers
    numbers.sort(numbers)
    # find the smallest and largest elements
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return smallest, largest
```