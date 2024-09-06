```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Keep track of the two closest numbers
    closest1 = float("inf")
    closest2 = float("inf")

    # Sort numbers to make sure that small values are closer to the reader
    for num in numbers:
        if num < closest1:
            closest1 = num
        elif num < closest2:
            closest2 = num

    # Return the two closest numbers
    return_list = [closest1, closest2]
    return_list
```
This solution defines a function find_closest_elements that takes a list of numbers as an input and returns a tuple of the two closest numbers in the list. It uses the sorting the to make sure that small values are closer to the reader and stores the two closest numbers in a list.

The function works by first initializing two variables, closest1 and closest2, to infinity. Then, it iterates through the numbers in the list and compares them to the current values of the two variables. It will then smaller number will the number is stored in the closest1 variable and the larger number is stored in the closest2 variable. Finally, the function returns a list of the two closest numbers and returns it.