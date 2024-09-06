```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    numbers.sort()
    smallest_num, largest_num = (numbers[0] , numbers[1])
    for i in range(len(numbers) - 1):
        if numbers[i] < smallest_num:
            smallest_num = numbers[i]
        if numbers[i] > largest_num:
            largest_num = numbers[i]
    return smallest_num, largest_num
```
The function `find_closest_elements` takes a list of numbers as input and returns a tuple with the two closest elements in the list, with their corresponding orders. The function sorts the both elements of the input list and selects the smallest and largest elements, and returns them in order.