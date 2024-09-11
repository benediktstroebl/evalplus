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
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This Python script defines a function `has_close_elements` that checks if there are any two numbers in the given list that are closer to each other than the specified threshold. The function iterates over all pairs of numbers in the list and returns True as soon as it finds a pair that satisfies the condition. If it checks all pairs without finding a close pair, it returns False.

The function's time complexity is O(n^2), where n is the number of elements in the list, because it uses nested loops to compare all pairs of numbers. This may be inefficient for large lists, but it meets the requirements of the problem. 

Please note that this code doesn't handle potential errors, such as lists with less than two elements or NaN values. Depending on the specific requirements of your application, you may want to add error checking code to handle these cases.