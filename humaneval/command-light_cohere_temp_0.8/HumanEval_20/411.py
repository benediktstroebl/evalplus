Here is a Python script that includes a self-contained function that solves the problem you've described:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    from typing import Tuple
    from math import sqrt

    # Sorting numbers in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    # Find the two closest elements
    i = 0
    while i < len(sorted_numbers) - 1:
        j = i
        while j < len(sorted_numbers) and sorted_numbers[j] < sorted_numbers[i]:
            j += 1
        if j == len(sorted_numbers):
            closest_elements = (sorted_numbers[i], sorted_numbers[i])
            break
        elif sorted_numbers[j] < sorted_numbers[i]:
            closest_elements = (sorted_numbers[j], sorted_numbers[i])
            j += 1
        i += 1
    return closest_elements

```

This code defines a function `find_closest_elements` that takes a list of numbers as an input and returns a tuple containing the two closest numbers in that list.  The function uses sorting and a while loop to find the two closest numbers in the list and returns them in that order.