Here's a self-contained Python function that solves the problem you described: 

```python
import math
def find_closest_elements(numbers: List[float]):
    """ Returns the two closest elements in the list and the separation between them """
    dist = [math.sqrt(x**2 - for x, y in zip(numbers, numbers[1:]))]
    return dist[0], dist[1]
```
This function calculates the squared distance between each pair of elements in the list, and stores the result in a list called `dist`. Then, it returns the smallest and the largest values in `dist`, representing the separation between the closest elements.