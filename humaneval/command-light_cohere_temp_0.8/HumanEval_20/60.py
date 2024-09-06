```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)
    """
    if len(numbers) < 2:
        raise ValueError("The list of numbers must have at least two elements")
    
    numbers.sort()
    stability=True
   
    smallest = numbers[0]
    largest = numbers[-1]
    
    for i in range(1, len(numbers)-1):
        smallest = numbers[i] if numbers[i] < smallest else smallest
        largest = numbers[i] if numbers[i] > largest else largest
    
    return smallest, largest
```
This function takes a list of numbers as input and returns a tuple of the two closest elements in the list. This is two closest elements are determined using the "point,  shoot" method, which compares the current element with the smallest and largest elements in the list.