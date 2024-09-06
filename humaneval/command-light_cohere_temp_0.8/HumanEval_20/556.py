Here is the Python code:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initialising variables
    closest1 = float("inf")
    closest2 = float("inf")
    first = second = 0
    # looping to compare each element of the list with the other
    for num in numbers:
        # if the current number is smaller than the other, update the variables
        if num < closest1:
            closest1 = num
            first = num
        elif num < closest2:
            closest2 = num
            second = num
        # return the first and second values, in case the list is length two
        if len(numbers) > 2:
            return (closest1, closest2)
        # returning the closest number
        return min(closest1, closest2)
```

This code uses a function called `find_closest_elements` to solve the problem. It takes two supplied list of numbers and returns the two closest elements in the list, with the smaller number in front. The code uses the critical path to compare each element of the list with the other elements, to find the closest pair of elements in the list.