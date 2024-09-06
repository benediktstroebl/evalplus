```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the two closest numbers
    smallest = float('inf')
    second_smallest = 0.0
    # Initialize the New values until you are not equal, they are closest to each other.
    function <first_number>(numbers):
        if numbers[0] < numbers[1]:
            smallest = numbers[0]
        else:
            smallest = numbers[1]
        second_smallest = numbers[0]
    function <second_number>(numbers):
        if numbers[0] < numbers[1]:
            second_smallest = numbers[0]
        else:
            second_smallest = numbers[1]
    # Return the two closest numbers
    return (smallest, second_smallest)
```