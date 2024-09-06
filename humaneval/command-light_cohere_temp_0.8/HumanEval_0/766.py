```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """ Return a boolean
    array(numbers)
    if len(set(array(numbers))) < 2:
        return False
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# Test
my_list = [1.0, 2.0, 3.0, 0.8, 4.0, 5.0]
my_close_elements(my_list, 0.8)
print(has_close_elements(my_list, 0.8))  # True 
```