```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    if any two elements in numbers[0:num-1] are closer to each other than threshold:
        return True

    numbers.sort(reverse=True)
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1] <= threshold:
            return True
    return False
```
This function takes two arguments: a List of numbers and a threshold. When the list is sorted in ascending order, this function checks if any two elements in the list are closer than the threshold. If so, the function returns True, which means that there are elements that are close enough and returns True. If not, the function returns False.