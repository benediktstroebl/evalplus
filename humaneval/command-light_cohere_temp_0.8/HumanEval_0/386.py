```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # check if in given list, are any two numbers closer to each other than threshold
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False

# test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3]

result = has_close_elements(numbers, 0.0)
print(result) # True

``` 
This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer than a certain threshold.  The function then returns `True` if this is the case, and `False` otherwise.  The test the function by comparing the elements of the list with a given threshold.