```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i+1] <= threshold:
            return True
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.2))  #
 old and new
print(has_close_elements([1.0, 2.0, 3.0], 0.2))  
 print(has_close_elements([1.0, 2.0, 3.0], 0.4)) # 1.1 < 0.7

We can also pass more complex test cases by changing the threshold or adding new elements.