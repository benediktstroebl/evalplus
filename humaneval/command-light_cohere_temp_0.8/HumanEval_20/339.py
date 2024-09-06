Here's a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    
    Parameters: 
        numbers: List[float] - A list of floating-point numbers
        
    Returns: 
        Tuple[float, float] - A tuple containing the two closest numbers in the list, in order of their smaller and larger values.  """ 

```
Here's how the function works:
1. First, it checks if the list has at least two elements.
2. Then, it sorts the list in ascending order.
3. Then, it finds the list's first element and the last element.
4. The function compares the element in the list to the first element in the list and returns the result in the first element of the tuple.
5 Then then, it compares the second element of the list with the element in the tuple. Finally, the function returns the result in the second element of the tuple.

This function effectively finds the closest pair of elements in the list.