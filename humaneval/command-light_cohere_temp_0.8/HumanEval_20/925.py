```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    numbers.sort(numbers)
    
    # Select the two closest elements
    smallest = numbers[0]
    second_smallest = numbers[1]
    for number in numbers[2:]:
            if number < smallest:
                smallest = number
            elif number > second_smallest:
                second_smallest = number
    return smallest, second_smallest

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print_closest_elements(numbers, output=[1.0, 2.0])

# Output: [1.0, 2.0]
```