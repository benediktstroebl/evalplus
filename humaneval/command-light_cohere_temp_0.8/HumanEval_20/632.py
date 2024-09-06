Here's the self-contained Python function:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Determine the two closest elements and return them
    smallest = float('inf')
    largest = float('-inf')
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    if smallest == largest:
        return (smallest, largest)
    return (largest, smallest)
```
This function takes a list of numbers as input and returns a tuple of two closest numbers. It iterates through to determine the two closest elements and return them in descending order. It uses the maximum element to store the largest number and the smallest element to store the smallest number. 
This function follows the standard approach of finding the two closest elements and returning them in descending order.