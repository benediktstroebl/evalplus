Here's a self-contained Python script that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two of the numbers in the list that are closest to each other, and returns them in order of decreasing number. The numbers are assumed to be floating point, and must be passed in as a List[float]. """
    """
    # Define a tuple to hold the results
    result = ()

    # Sort the numbers in descending order
    numbers.sort(key=lambda x: -x)

    # Get the first two numbers in the sorted list
    first = next(numbers)[0]
    second = next(numbers)[1]

    # Add the two numbers in the result tuple
    result = (first, second)

    # Return the result tuple
    return result
```

This code defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two numbers in the list that are the closest to each other. The function uses the sorting the `next()` function to retrieve the first and second elements from the list and then uses the tuple unpacking technique `()` to create a tuple with the two values. 

The code also uses the `sort()` function to sort the list of numbers in descending order based on their values.