Here is a self-contained Python script that solves the problem of finding the closest elements from a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the input list of numbers in ascending order
    numbers.sort(numbers)
    
    # Take the first element in the sorted list
    first = numbers[0]
    
    # Search the sorted list for the second element with the same value as the first element
    for i, n in enumerate(numbers[1:], start=1):
        if numbers[i] == first:
            second = n
            break
        if second is None:
            return (first, second)
    
    return (first, second)

```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two closest elements in the list, which are then returned in descending order (smaller number, larger number). 

The function sorts the input list of numbers in ascending order using the `sort` function. Then, it searches the the sorted list for the second element with the same value as the first element, starting from the second element in the list. 

Finally, it returns the tuple of the two closest elements.