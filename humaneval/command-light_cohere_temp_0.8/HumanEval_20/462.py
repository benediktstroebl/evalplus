```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two closest elements from the input list, and returns them in order (smaller number, larger number).
    """
    numbers = sorted(numbers, key=lambda x: x[0])
    return numbers[0:1]
```
This function takes a list of numbers as input and sorts the list based on the first element, then selects and returns the first two elements in order. This ensures that the needed pair is returned.

The function could be improved to accept a range of numbers instead of just a list of numbers. This would allow for more flexibility and would reduce the need to sort the list.

Additionally, you could enhance the function by adding a parameter to specify the maximum length of the list to ensure that the function works correctly with large inputs.