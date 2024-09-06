```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    # Store the
    first smaller number
    if numbers[0] < numbers[1]:
        return True

    # Start from the second element
    for i in range(1, len(numbers)):
        # Store the current smaller number
        current_smaller = numbers[i]

        # Move to the next element
        i += 1

        # Check if the current element is less than the threshold
        if current_smaller < threshold:
            return True

    return False

# Test
if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0], 0.3): True
 test if not has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.3])

``` 
The above Python script defines a function called `has_close_elements` that checks whether any two elements in a list of numbers are closer than a given threshold. It works by first storing the smaller number between the first two elements in a list, and then starting from the second element, it checks if the current element is less than the threshold. The function returns True if any of these conditions are met.