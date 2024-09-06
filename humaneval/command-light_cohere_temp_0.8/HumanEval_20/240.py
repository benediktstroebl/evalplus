Here's the code:
```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    # Step 1: Sort the input list
    sorted_numbers = sorted(numbers)
    # Step 2: Find the first and second elements of the sorted list
    first_element = sorted_numbers[0]
    second_element = sorted_numbers[1]
    # Step 3: Return the first and second elements in order of the smaller number
    return first_element, second_element
```
This code provides a self-contained function that takes a list of numbers, finds the two closest elements, and returns them in order of smaller number, larger number.