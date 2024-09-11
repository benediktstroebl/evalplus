```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of float numbers.
    threshold (float): The minimum distance required between any two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize a variable to store the result
    result = False
    
    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is less than or equal to the threshold, update the result and break the loop
        if difference <= threshold:
            result = True
            break
    
    # Return the result
    return result


# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list of numbers and then iterates over the sorted list, checking if the difference between any two adjacent numbers is less than or equal to the threshold. If such a pair of numbers is found, the function returns `True`; otherwise, it returns `False`. The script also includes two test cases to demonstrate the usage of the function.