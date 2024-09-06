```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    if any( abs(x1 - x2) <= threshold for x1, x2 in numbers)
    return True

#Example usage
numbers = [1.0,2.0,3,8,4,5,0]
threshold = 0.1
result = has_close_elements(numbers,threshold)
print(result) # True
```
This script defines a function has_close_elements that takes a list of numbers and a threshold as input and returns a boolean value indicating whether any two numbers in the list are closer than the threshold. 

The function uses the "any" function to check if there are any elements in the list that have a difference less than or equal to the threshold, and then return true.