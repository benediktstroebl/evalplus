```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The maximum allowed distance between two numbers.

    Returns:
    bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference found so far to infinity
    min_diff = float('inf')
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Calculate the absolute difference between the current number and the previous one
        diff = abs(numbers[i] - numbers[i-1])
        
        # Update the minimum difference found so far if the current difference is smaller
        min_diff = min(min_diff, diff)
        
        # If the minimum difference found so far is less than or equal to the threshold, return True
        if min_diff <= threshold:
            return True
    
    # If we've iterated over the entire list and haven't found any two numbers closer than the threshold, return False
    return False

# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Should print: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Should print: True
```