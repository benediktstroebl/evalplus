Here is a self-contained Python script that solves the problem you have provided:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Find two closest elements and return them in order of their values.
    """
    def compare_elements(element1: float, element2: float) -> Tuple[float, float]:
        return (element1, element2)
    if numbers[0] <= element1:
        return (element1, numbers[0])
    elif numbers[1] <= element2:
        return (numbers[1], element2)
    else:
        return (numbers[0], element1)

result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 2])
print(result)
```
This code defines a function called `find_closest_elements` that takes a list of numbers as an input parameter and returns a tuple with the two closest elements in the list.

The `compare_elements` function takes two elements of a list and returns a tuple with the two elements, which is then used by the `find_closest_elements` function to find the two closest elements in the list.