### Solution
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    
    # Sort the list of numbers
    numbers.sort()
    
    # Initialize a variable to track whether close elements have been found
    close_elements_found = False
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(numbers)):
        # Calculate the difference between the current number and the previous one
        difference = numbers[i] - numbers[i - 1]
        
        # If the difference is less than the threshold, close elements have been found
        if difference < threshold:
            close_elements_found = True
            break
    
    return close_elements_found

# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
### Explanation

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list of numbers and then iterates over it, calculating the difference between each number and the previous one. If the difference is less than the threshold, it sets `close_elements_found` to `True` and breaks out of the loop. The function returns `True` if close elements have been found, and `False` otherwise.

The test cases at the end of the script demonstrate the function's behavior.