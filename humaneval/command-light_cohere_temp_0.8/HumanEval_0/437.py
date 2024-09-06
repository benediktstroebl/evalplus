```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   0) 1.1

   0)0.1 and the0.8
   
   0} has close to each.

    # If check:
    if len(numbers) == 2 and numbers[0] - numbers[1] <= threshold:
        return True
    else:
        return False
    # end of check

    return True if has_close_elements(numbers[1:], threshold) else False

```
This function takes two parameters: numbers, which is a list of float numbers and threshold, which is a float number. The function returns True if any two numbers in the list are closer to each other than the threshold, otherwise, it returns False.