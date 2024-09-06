```python
from typing import List
def find_closest_elements(numbers: List[float]):
    x, y = (min(numbers), max(numbers))
    closest = [x, y]
    for i in range(1, 5):
        current = (numbers[i] - x) ** 2 + (numbers[i] - y) ** 2
        if current < closest[0]:
            closest[0] = current
            closest[1] = i
    return closest[0], closest[1]

```
This function takes a list of numbers as an input and returns a tuple of the closest pair of elements. It uses the formula to calculate the distance between any two elements, then selects the smallest and largest elements from the list, and iterates to the second smallest and second largest elements.