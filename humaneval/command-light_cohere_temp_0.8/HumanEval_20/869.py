Here is a self-contained Python script that solves the problem you've described:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Check for at least two elements in the list
    if len(numbers) < 2:
        return numbers, None
    
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Get the two closest numbers
    left_index = 0
    right_index = len(sorted_numbers) - 1
    while left_index <= right_index:
        current_number = sorted_numbers[left_index]
        next_number = sorted_numbers[right_index]
        
        # Compare the two numbers and find the smallest
        if current_number < next_number:
            return current_number, next_number
        left_index += 1
        right_index -= 1
    
    return None, None

# Example usage:
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0])

return (2.0, 5.0),
```