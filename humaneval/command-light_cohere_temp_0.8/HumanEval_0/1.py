```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    # Sorting theator's list in ascending order
    numbers.sort()

    least 2 elements that can be compared with each other.
    # Looping array through first element to second and so on, until the current element
    # does not reach the given threshold.
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] < threshold:
            return True
    return False

# Test cases
numbers1 = [0.3, 0.0, 1.0, 0.0]
numbers2 = [0.0, 2.0, 3.0, 4.0, 5.0, 2.0]
numbers3 = [1.0, 2.0, 3.0, 4.0]
numbers3 = [1.8, 2.0, 3.0, 4.0, 5.0]
numbers3 = [0.3, 0.0, 2.0, 0.0] are numbers close different a elements

print(has_close_elements(numbers1, 0.0))  # This result should be True
)
print(has_close_elements(numbers2, 0.3))  #This result should be False
```
This Python script defines a function called has_close_elements that checks if any two numbers in a given list are closer to each other than a given threshold. The function takes in a list of numbers and a threshold as input, and returns a boolean value indicating whether there are any such pairs of numbers in the list. The script also includes test cases to demonstrate the functionality of the function.