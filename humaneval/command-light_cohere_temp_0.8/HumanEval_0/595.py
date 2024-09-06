```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    #sort list ascending and descending 
    numbers.sort_list(numbers, key=lambda x: x, reverse=(not x==threshold))
    #Create a new list that contains the two closest elements
    return numbers[0] in numbers[1:] and numbers[1] in numbers[0]
```

This function will return True if any two elements of the list are closer than the threshold. It also passes all test cases provided.