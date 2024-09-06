Here is a self-contained Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    from sorted import key_pairs_from_sorted
    """
    # Sort the list of numbers
    sorted_numbers = key_pairs_from_sorted(numbers)

    # Initialize variables
    closest1 = float("inf")
    closest2 = float("-inf")

    # Loop through the sorted list and find the smallest and largest numbers
    for (num1, num2) in sorted_numbers:
        if num1 < closest1:
            closest1 = num1
        elif num2 < closest2:
            closest2 = num2

    # Return the two closest numbers in order of their difference (larger number, smaller number)
    return (closest1, closest2)
```

This code defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two closest numbers in the list. The function first sorts thees the list of numbers using the `key_pairs_from_sorted` function. It then initializes two closest variables to infinity and loops through the sorted list, comparing each pair of numbers to the current closest numbers. Finally, it returns the smallest and largest numbers, in that order.