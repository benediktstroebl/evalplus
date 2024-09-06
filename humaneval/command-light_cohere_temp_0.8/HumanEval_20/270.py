Here's a self-contained Python script that solves the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize a list to store the two closest elements.
    closest_elements = [float("inf"), float("-inf")]
    for num in numbers:
        if num < closest_elements[0]:
            closest_elements[0] = num
        elif num > closest_elements[1]:
            closest_elements[1] = num
        else:
            # Check for duplicate elements
            if closest_elements[0] == num:
                closest_elements.remove(closest_elements[1])
            elif closest_elements[1] == num:
                closest_elements.remove(closest_elements[0])
            else:
                closest_elements[1] = num
                closest_elements[0] = num
    return closest_elements
```

The function `find_closest_elements` takes a list of numbers as an argument and returns a tuple containing the two closest elements in order. It uses a (smaller number, larger number) rule to determine which two elements are the closest. 

The script uses the `remove` method to remove the duplicate elements, so the result is a tuple of the two distinct closest elements.