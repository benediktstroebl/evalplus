```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    # Sort the list of numbers
    numbers.sort(lambda ax: x, y: x - y)
    # Calculate the distance between the first and second elements in the sorted list
    first_element, second_element = numbers[0], numbers[1]
    distance = (first_element - second_element)**2
    # Return the elements that are the closest to each other and their order
    return distance, second_element
```

This function uses the Pythagorean theorem to calculate the distance between two points. The first element is the second element in the list. The function then sorts the elements in ascending order and returns the smaller element and the distance between the two elements. The test passed to the function passes a list with at least two elements, which the function uses to determine the closest elements.