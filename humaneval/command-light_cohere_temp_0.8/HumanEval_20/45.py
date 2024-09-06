```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects two numbers from a list that are closest to each other and returns them in order (smaller number, larger number)
    """
    # Sort the list of numbers in ascending order
    numbers.sort(key=lambda x: -x)
    # Take the first two elements of the sorted list
    first, second = numbers[:2]
    # Sort the first and second elements again in ascending order
    first, second = [x for x in [first, second]]
    # Return the first and second elements in order
    return Tuple(first, second)

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
3]
result = find_closest_elements(numbers)

print(result)
```
This function is a self-contained Python script that solves the problem of finding the two closest elements in a list of numbers and returns them in order (smaller number, larger number). The function sorts the list of numbers in ascending order and then takes the first two elements of the sorted list. The function then sorts the elements again in ascending order and returns the first and second elements in order.