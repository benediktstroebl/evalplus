```markdown
### Find Closest Elements in a List of Numbers

This Python script finds two numbers in a list that are the closest to each other.
#### Code

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other 
    and return them in order (smaller number, larger number).
    
    Args:
        numbers (List[float]): A list of numbers.
    
    Returns:
        Tuple[float, float]: A tuple of two closest numbers.
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")
    
    # Sort the list
    numbers.sort()
    
    # Initialize the closest pair and the minimum difference
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])
    
    # Iterate over the list to find the closest pair
    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i + 1] - numbers[i])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Example use cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

This script first checks if the list has at least two elements. If not, it raises a `ValueError`. Then, it sorts the list. The closest pair is initially set to the first two elements and the minimum difference is set to the absolute difference between these two elements. The script then iterates over the list to find the closest pair. If a pair with a smaller difference is found, it updates the closest pair and the minimum difference. Finally, it returns the closest pair.