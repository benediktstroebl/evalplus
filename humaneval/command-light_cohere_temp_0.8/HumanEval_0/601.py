```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   FF)
   0] = False
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return True
    return False

# Test the function
test_data = [1.0, 2.0, 3.0, 0.0, 0.0, 5.0]
print_close_elements(test_data, 0.0) # Should return True

```
This script defines a function called has_close_elements, which takes a list of numbers and a threshold as input and returns a boolean indicating whether any two numbers in the list are closer than the given threshold. The function uses a nested loop to iterate through the list, and checks if the difference between each number and the next number is less than or equal to the threshold.