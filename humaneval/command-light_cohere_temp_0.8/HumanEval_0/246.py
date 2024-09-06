Here's the answer:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :return True if any two elements in numbers are closer than threshold, otherwise False
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False

# Test cases goes here
numbers = [1.0, 1.0, 2.0, 3.0, 4.0, 5.0]
has_close_elements(numbers, 0.0) # False

```
The has_close_elements function takes a list of numbers and a threshold as input, and returns True if any two elements in the list are closer than the threshold, otherwise, it returns False. The function uses a two nested loops to compare each element in the list with all the remaining elements, and returns True if any comparison is true.