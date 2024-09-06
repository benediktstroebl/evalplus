Here is the provided Python script that solves the problem:
```python
from typing import List
from typing import Tuple
def find_closest_elements(numbers: List[float]):
    # Sort the numbers in descending order
    numbers.sort(reverse=True, key=numbers.__iter__()[::-1])
    
    # Find two closest elements
    smallest = float('inf')
    largest = float('-inf')
    for i in range(len(numbers) - 1):
        current = numbers[i]
        if current < smallest:
            smallest = current
        if current > largest:
            largest = current
    
    # Return the two closest numbers
    return Tuple(smallest, largest)
```
This code defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two closest numbers in the list. It sorts the numbers in descending order using the `sort()` function and then iterates over the list to find the two closest numbers. The function uses the unique approach to finding the two closest elements.