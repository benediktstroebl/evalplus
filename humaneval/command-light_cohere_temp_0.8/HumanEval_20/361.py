Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two elements from the input list that are the closest to each other, and returns them in order (smaller number, larger number).
    
    Parameters:
        numbers: List[float] - List of floating-point numbers
    
    Returns:
        Tuple[float, float] - A tuple containing the two closest elements in order of their values.
    """
    def sort_numbers(numbers: List[float]):
    # Sort the input list in ascending order
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0:len(sorted_numbers)//2]

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
```

This function first sorts the list of numbers in ascending order, then it returns the first half of the sorted list, which will be the two smallest numbers. The remaining half of the sorted list will be the two largest numbers.

Note that this function assumes that the input list has at least two elements.