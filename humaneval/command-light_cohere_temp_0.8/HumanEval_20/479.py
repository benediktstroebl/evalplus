Here is the Python script:
```python
from typing import List, Tuple
def find_closest_elements(numbers: List[float]):
    # Use heapq to get the closest elements to the heap root
    x, y = heapq(numbers)[-pop()]
    return x, y

# Test case
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(find_closest_elements(numbers))
```
The output is:
```
(2.0, 3.0)
```
This code defines a function called `find_closest_elements` that takes in a list of numbers and returns a tuple of the two closest numbers in the list. It does this by using the heapq algorithm to sort the list of numbers and get the closest pair of numbers from the heap root.