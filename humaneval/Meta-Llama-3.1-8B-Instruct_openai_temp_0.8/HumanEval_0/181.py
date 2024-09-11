```markdown
### Solution to Problem: Check for Close Elements in a List of Numbers

#### Problem Description
Check if in given list of numbers, are any two numbers closer to each other than given threshold.

#### Code
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    
    Args:
        numbers (List[float]): A list of float numbers.
        threshold (float): The minimum distance between two numbers to be considered close.
    
    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate through the list of numbers
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If the numbers are close, return True
            return True
    
    # If no close elements are found, return False
    return False

### Example Usage
if __name__ == "__main__":
    # Test the function
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Expected output: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Expected output: True
```

#### Explanation
The function `has_close_elements` takes two parameters: a list of numbers and a threshold. It sorts the list in ascending order and then iterates through it to check if any two consecutive numbers are closer than the threshold. If a pair of close numbers is found, it returns `True`. If it iterates through the entire list without finding any close numbers, it returns `False`.