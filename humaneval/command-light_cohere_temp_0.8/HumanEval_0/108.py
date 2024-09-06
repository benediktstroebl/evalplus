```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # Use two pointers to compare the first two elements
    # and check if their difference is less than threshold
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[0]:
            numbers[0] = numbers[i]
    else:
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[0]:
                    numbers[0] = numbers[j]
                    return True
            break

    # return False
    return False

# Test the function
numbers = [1.0, 2.0, 3.0, 0.0, 4.0, 5.0, 2.0, 6.0, 8, 9.5, 3.0, 8, 8, 3, 7, 5, 6, 7, 9]
print(has_close_elements(numbers, 0.8))  # This) # True
``` 
This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It uses the pointers technique to loop through the list, comparing the first element with the next elements. If any element in the list is smaller than the current element, the function updates the first element to this value. If the loop completes without finding a pair that satisfies the condition, the function returns `False`. 

The script then provides a test case with a list of numbers and a threshold, and prints the result. The expected output is `True`.