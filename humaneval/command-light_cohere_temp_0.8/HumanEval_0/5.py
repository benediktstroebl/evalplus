```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    list of all pairs is created using the combination list() function.
    pairs = list(combination(numbers, rrange(len(numbers))))
    pairs = list(zip(numbers, pairs))
    check = [x for x in zip(numbers, [y for y in numbers if y - x < threshold]))]
    return check == [x for x in numbers if x in check]
```
This function works by: 
- Creating a list of all possible pairs in the numbers list, using the combination function.
- Compressing each pair against the threshold
- Storing the results in a list of check values
- Finally, the function returns True if any of the check values is in the numbers list, otherwise it returns False.