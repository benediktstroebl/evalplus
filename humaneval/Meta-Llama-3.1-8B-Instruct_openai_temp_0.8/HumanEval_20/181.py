### Closest Pair of Numbers
#### Problem Description
Find two numbers in a list that are the closest to each other and return them in order (smaller number, larger number).

#### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find two numbers in a list that are the closest to each other and return them in order (smaller number, larger number).
    
    Args:
        numbers (List[float]): A list of numbers of length at least two.
    
    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in order.
    """
    
    # Check if the input list is empty or contains less than two elements
    if len(numbers) < 2:
        raise ValueError("The input list must contain at least two elements.")
    
    # Sort the list of numbers
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the current difference is smaller than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
# Output: (2.0, 2.2)

print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
# Output: (2.0, 2.0)
```
This script defines a function `find_closest_elements` that takes a list of numbers as input, sorts the list, and then iterates over the sorted list to find the pair of numbers with the smallest difference. The function returns this pair as a tuple. The script also includes example usage to demonstrate the function's behavior.