```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
   
    :type numbers: List[float]
    :type threshold: float
    :rtype: bool
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```
This code implements a function called **`has_close_elements`** that checks if any two numbers in a given list are closer than a certain threshold. It does this by comparing each number in the list with the remaining numbers, and returns **`True`** if any two numbers are closer than the threshold. The function returns **`False`** otherwise.