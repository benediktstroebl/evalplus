```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Returns: boolean indicating whether list contains any two numbers that are closer than threshold.
    """
    given numbers: List[float]
    threshold: float

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i]-numbers[j]) < threshold:
                return True
    return False
```

This function utilizes a nested loop to compare pairs of numbers in the list. The outer loop iterates through the range of the list, and the inner loop iterates over the adjacent pairs of numbers. The function then checks if the absolute difference between the current pair of numbers is less than the threshold. 
If the condition is met, the function returns True, indicating that there are elements in the list that are closer than the given threshold. 
If the function completes all loops without returning True, it returns False.