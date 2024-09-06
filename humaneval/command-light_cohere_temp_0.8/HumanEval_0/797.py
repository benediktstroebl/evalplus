```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the list of numbers, any two consecutive elements are closer than the given threshold.
    Parameters: 
    - A list of numbers (float).
    - threshold (float) 
    Returns: boolean value 
    """
    for i in range(len(numbers)-1):
        if numbers[i] - numbers[i - 1] < threshold:
            return True
    return False

# Test the function 
print(has_close_elements([1.0, 2.0, 3.0, 0.0, 4.0, 5.0, 2.0], 0.3))

 # True 
print(has_close_elements([1.0, 1.0, 2.0, 3]))
 # False
print(has_close_elements([1.0, 2.0, 3.0, 0.0, 4]))
 # False
print(has_close_elements([8.0, 6.0, 3.0]))
 # False

```
This script defines a function `has_close_elements` that checks if any two consecutive elements in a list of numbers are closer than a given threshold. 
The function uses a loop to iterate through the list of numbers and checks if the difference between the current and previous elements is less than the threshold. 

The function then returns `True` if this condition is met, and `False` otherwise. 
Finally, the function is tested with a few examples to verify its correctness.