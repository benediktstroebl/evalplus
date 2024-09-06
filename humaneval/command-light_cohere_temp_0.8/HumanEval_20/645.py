```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    Returns a tuple containing both numbers.
""
    # Sort the list of numbers to make sure we have a valid order of elements.
    numbers.sort()
    stability=True
    least, two, most close, numbers in the list.
    return_two = numbers[0] - numbers[1]
    return (numbers[0], numbers[1])
```
This function takes a list of numbers as input and returns a tuple containing the two numbers that are closest to each other. The function first sorts the duplicate the list to ensure that the order of the elements is valid. Then, the function uses the difference between the first and second elements of the list to determine which is the smaller number. The function then subtracts the second element from the first element, and stores the result in the variable `result_two`. Finally, the function returns a tuple containing the first element and the second element.