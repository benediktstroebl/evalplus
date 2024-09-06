```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        return None, None
    # Sort the list of numbers
    numbers.sort(key=lambda n: -n)  # Descending order is necessary
    # Get the first and second elements from the sorted list
    first, second = numbers[0], numbers[-1]
    # Return the elements in the order of the closer number, larger number
    return first, second
```
This function accepts a list of numbers as an argument and returns a tuple of two closest elements. It determines whether the saw a list of at least two numbers. It returns None, None if the list has fewer than two elements. The function then sorts the list in descending order and retrieves the first and last entries. Finally, it returns the tuple of these two elements in ascending order.