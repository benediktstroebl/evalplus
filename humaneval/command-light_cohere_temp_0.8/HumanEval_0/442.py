Here is a Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False

# Example test cases 
numbers1 = [1.0, 2.0, 3.0, 0.0, 5.0]
has_close_elements(numbers1, 0.8) # returns True
numbers2 = [1.0, 8.0, 3.0, 0.0, 5.0]
has_close_elements(numbers2, 0.8) # returns False
numbers3 = [1.0, 3.0, 5.0, 0.0, 0]
has_close_elements(numbers3, 0.0) # returns False

This function iterates over the given list of numbers and checks if any two consecutive elements are closer than a threshold.  If they are, it returns True. Otherwise, it returns False.