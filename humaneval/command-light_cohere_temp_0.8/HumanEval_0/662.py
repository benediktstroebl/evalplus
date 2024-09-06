Here's the answer:
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
``` 
This code defines a function `has_close_elements` that checks if any two consecutive elements in the list are closer than a given threshold. The function uses a loop to iterate over the list and another loop to check each pair of consecutive elements. The condition is checked if the difference between the current element and the next element is smaller than the threshold. The function returns `True` if any such of these conditions is met, otherwise it returns `False`.