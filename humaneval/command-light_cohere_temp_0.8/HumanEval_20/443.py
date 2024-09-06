```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # initialise variables
    min1 = float("inf")
    max1 = float(-inf)
    closest = (0.0, 0.1)
    # loop for index, i in range(len(numbers)):
        current1 = numbers[i]
        current2 = numbers[(i + 1) % len(numbers)]
        # find the smallest number
        if current1 < current2:
            min1 = current1
            max1 = current2
        elif current1 > current2:
            min1 = current2
            max1 = current1
        else:
            closest = (min1, max1)
    # return the closest numbers
    return closest
```