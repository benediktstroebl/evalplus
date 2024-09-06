Here is a self-contained Python script that solves the problem of checking if any two numbers in a list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # type checking for parameters
    if not isinstance(numbers, List) or not all(isinstance(num, float) for num in numbers):
        raise TypeError("Input must be a list of numbers")
    # sort the list
    numbers.sort()
    result = numbers[::]
    # find two closest elements
    min_distance = 1e9
    max_distance = -1e9
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            current_distance = numbers[i] - numbers[j]
            if current_distance < min_distance:
                min_distance = current_distance
            if current_distance > max_distance:
                max_distance = current_distance
    # return result
    return min_distance <= threshold and max_distance <= threshold

```
This code defines a function called has_close_elements that takes in two parameters: a list of numbers and a float threshold. It then checks if the the list of numbers is valid, then sorts the list of numbers. It then finds the first and second closest elements in the list and returns true if both numbers are within the threshold of each other, and false otherwise.