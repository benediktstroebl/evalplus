```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    This function takes in a list of numbers and returns a tuple of the two numbers in the list that are the closest to each other.
    return the smallest number, larger number.)
    The function works by sorting the list of numbers and selecting the two closest numbers. The first element of the list is then returned, followed by the second element of the list.

Test cases:
>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])
(2.0, 1.0) 
 expected output)
```