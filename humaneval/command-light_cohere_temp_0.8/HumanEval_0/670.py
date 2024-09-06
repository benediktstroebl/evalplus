Here's a solution:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False

# Test
my_numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 0.0, 0.0, 3]

result = has_close_elements(my_numbers, 0.0)  # True
``` 
This function uses a nested loop to check if any two consecutive elements in the list are closer than the given threshold.  The function returns True if there are any such elements, indicating that the list has at least one pair of elements that are close to each other.