```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple of the two numbers that are closest to each other and in order of those two numbers. 
    numbers: List[float] 
    closest_1 = float('inf')
    closest_2 = float('-inf')
    for n in numbers:
        if n > closest_1 and n < closest_2:
            closest_1 = n
            closest_2 = n
    return closest_1, closest_2
``` 
This solution uses the list of numbers as input and then selects two elements from it that are the closest to each other and returns them in order (smaller number, larger number). 
The function works by comparing each number in the list with the current closest numbers, and updates the values of closest_1 and closest_2 accordingly. 
At the end of the loop, it returns the two numbers that were selected.