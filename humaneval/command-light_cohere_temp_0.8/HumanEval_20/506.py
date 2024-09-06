```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Selects two closest elements in the list and returns them in order (smaller number, larger number)
    """
    # Sort the list of numbers
    sorted_numbers = [num for num in numbers if num not in [0.0, float("inf")]]
    
    # Get the two closest elements
    first_index = sorted_numbers[0] if len(sorted_numbers) >= 2 else len(sorted_numbers)
    second_index = second_index = 0
    while first_index < len(sorted_numbers) and second_index < len(sorted_numbers) and sorted_numbers[first_index] <= sorted_numbers[second_index]:
        first_index += 1
        second_index += 1
    
    # Return the two closest elements
    return sorted_numbers[first_index], sorted_numbers[second_index]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
0]
result, tuple of two closest numbers to each other, in order

(1.0, 2.0)
```