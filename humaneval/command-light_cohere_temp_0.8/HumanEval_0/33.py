```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :return True if any set of two consecutive elements in numbers list are closer than the threshold, 
    else False
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```
This script defines a function that checks whether any two consecutive elements in a list are closer than a given threshold. It uses a two nested loops to compare each pair of elements and returns True if any of these conditions are met. The function is designed to be efficient and to handle large lists of numbers with a reasonable amount of computational overhead.