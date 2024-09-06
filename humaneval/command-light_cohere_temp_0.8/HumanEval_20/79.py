```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    numbers.sort(numbers)
    # Create a new list of the same length with the same elements, in this case numbers, sorted
    # now by the previous sort operation
    new_numbers = [numbers[i] for i in range(len(numbers))]
    # Sort the new list of numbers in descending order
    new_numbers.sort(new_numbers, reverse=True)
    # Check the length of the lists to ensure both are of length two
    if len(numbers) != 2 or len(new_numbers) != 2:
        raise ValueError("Input lists must be of length at least two")
    # Get the two closest elements from the new list and return them
    return new_numbers[0], new_numbers[1]
```