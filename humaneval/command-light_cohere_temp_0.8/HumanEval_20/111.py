```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple containing the two elements with the smallest and largest values in the list, in that order. """
    smallest = float('inf')
    largest = float('-inf')
    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
        else:
            return smallest, largest
    return smallest, largest
```
This code defines a function called **find_closest_elements** that takes a list of numbers as input and returns a tuple containing the two elements in the list that have the smallest and largest values, respectively. The function iterates over the smallest and largest values in the list, and updates the variables **smallest** and **largest** accordingly. The function returns the specific values when the condition is met, and the function returns the updated **smallest** and **largest** values.