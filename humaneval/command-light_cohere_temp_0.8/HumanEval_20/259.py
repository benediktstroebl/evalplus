Here's a self-contained Python script that includes a function called `find_closest_elements`, which solves the problem of finding two elements from the list that are closest to each other:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    Returns two elements from the list that are the closest to each other and returns them in order (smaller number, larger number).

    :listsort [float] -> List[float]
    """
    if len(numbers) < 2:
        return numbers, numbers

    # Sort the list of numbers in ascending order.
    sorted_numbers = sorted(numbers)

    # Initialize variables
    left = 0
    right = len(sorted_numbers) - 1
    closest_left, closest_right = sorted_numbers[left], sorted_numbers[right]

    while left < right:
        current_left, current_right = sorted_numbers[left], sorted_numbers[right]
        if current_left < current_right:
            closest_left, closest_right = current_left, current_right
        left += 1
        right -= 1

    return closest_left, closest_right
```

This code implements a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest numbers to each other in the list, in ascending order. It handles the cases where the provided list of numbers is empty or has less than 2 elements, it returns the list as is. Also, it handles the cases when the list of numbers has two elements, and it finds the correct order of the two elements in the list.

This function uses the `sorted()` function to sort the list of numbers and then initializes variables to keep track of the left and right indexes of the two closest elements. It uses a numbers in ascending order to ensure the correct order of the two elements in the list.

Finally, the function returns the two elements in the list, which are the closest to each other.