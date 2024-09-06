```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Take two numbers at the beginning of the sorted list
    first_element, second_element = sorted_numbers[0] + sorted_numbers[1]
    # Return the two closest elements
    return (first_element, second_element)

def test():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
    print("The result:", find_closest_elements([1.0, 2.0, 3.0, 4.0, 2]))
```