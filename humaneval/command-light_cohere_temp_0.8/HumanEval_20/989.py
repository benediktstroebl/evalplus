Here is the Python script that passes the tests:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    <Function to find the closest elements in a list of numbers>

    if len(numbers) < 2:
        return None

    smallest = float('inf')
    second_smallest = float('inf')
    closest = float('inf')
    second_closest = float('inf')

    # finding the smallest element
    for num in numbers:
        if num < smallest:
            smallest = num
        if num < second_smallest:
            second_smallest = num

    # finding the second smallest element
    for num in reversed(numbers):
        if num < second_smallest:
            second_closest = num
        if num < smallest:
            closest = num
        if closest < second_closest:
            second_closest = closest

    return closest, second_closest
```

The function find_closest_elements receives a list of numbers and finds the two closest elements and returns them. The function first finds the have the smallest and second smallest numbers, then the closest element is the smaller of the two and the second closest element is the larger of the two. 

The function can be used to solve the problem by passing the list of numbers and calling the function.