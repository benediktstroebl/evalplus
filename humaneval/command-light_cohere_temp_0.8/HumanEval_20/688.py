```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    numbers = [1.0, 2.0, 3.0, 4]
   2])

    if len(numbers) < 2:
        return numbers

    # Sorting numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Getting the first two elements from the sorted list
    first_two = sorted_numbers[:2]

    # Calculating the distance between the elements
    distance1 = abs(first_two[0] - first_two[1])
    distance2 = abs(first_two[0] - second)

    # Choosing the smaller one as the first element
    if distance1 < distance2:
        closest_element1 = first_two[0]
        closest_element2 = first_two[1]
    else:
        closest_element1 = first_two[1]
        closest_element2 = first_two[0]

    return closest_element1, closest_element2

```
The provided Python code defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements from the input list. 

The function first checks if the input list has at least two elements. If not, it returns the list as is. Otherwise, it sorts the list in ascending order and extracts the first two elements. 

The code then calculates the distance between the two elements and chooses the smaller one to be the first element of the returned tuple. Finally, the function returns the two elements, which are the closest elements from the input list.