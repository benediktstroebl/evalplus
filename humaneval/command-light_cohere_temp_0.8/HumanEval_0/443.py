Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False
```
This function takes a list of numbers and a threshold as input and returns a boolean value indicating whether any two numbers in the list are closer than the threshold. The function uses a two nested for loops to iterate over all possible pairs of numbers in the list. 

Note that this function does not use the type hint for the `numbers` parameter, as it is supposed to be self-contained and does not need the actual data type.