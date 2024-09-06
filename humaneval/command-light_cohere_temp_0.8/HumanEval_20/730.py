Here's the code:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # sort the list
    numbers.sort(key=lambda x: -x)

    # find the first element
    smallest, larger = numbers[0], numbers[-1]
    # swap the elements
    numbers[0], numbers[-1] = numbers[-1], numbers[0]

    # return the first and second closest elements
    return smaller, larger
```
This code uses the `typing` module to import the `List` and `Tuple` classes, which are necessary to create a list and a tuple, respectively. This function takes a list of numbers, and then sorts it by its key function. The first element is then compared to the last element and the second element is swapped. Finally, the function returns the first and second closest elements.