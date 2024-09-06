```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = sorted(numbers)
    for i in range(1, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False
```
The above Python script defines a function called `has_close_elements` that takes two inputs: a list of numbers and a threshold value. It then sorts the in ascending order the numbers in the list and uses a nested loop to iterate through the sorted list. It checks if any two consecutive elements in the list are closer than the given threshold. If this condition is met, it returns `True`, indicating that there are elements in the list that are close to each other. 

If no such condition is met within the loop, it returns `False`, indicating that there are no such elements in the list.