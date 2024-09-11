```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of at least two floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers.
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = ()
    
    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        
        # Update the minimum difference and the pair of closest numbers if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair

# Example usage
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

In this script, the function `find_closest_elements` takes a list of numbers as input, sorts it, and then iterates over it to find the pair with the minimum difference. The pair of closest numbers is then returned. The script also includes two example use cases.