```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = sorted(numbers)
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] - numbers[i] <= threshold:
                return True
    return False

# Test
numbers = [1.0, 2.0, 3.0, 0.0, 5.0, 8]
return has_close_elements(numbers, 0.5))
``` 
This script defines a function called `has_close_elements` that takes in a list of numbers and a threshold as input and returns a boolean value indicating if any two elements in the list are closer than the threshold. The function uses a sorted() function to sort the input list of numbers and then uses a loop to iterate over the sorted list. The function then checks if the difference between the current element and the next element in the list is less than or equal to the threshold. The function then returns `True` if any of these conditions are met, otherwise it returns `False`.