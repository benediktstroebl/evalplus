Here is a self-contained Python script that solves the problem of finding the two closest elements in a list of floating-point numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    numbers.sort(numbers)

    # Take the first and second elements of the sorted list
    first, second = numbers[0], numbers[1]
    # Calculate the distance between the first and second elements
    first_value, second_value = (first - second) ** 2
    # Return the first and second elements and the calculated distance
    return first, second, first_value + second_value

```
This function takes a list of numbers as input and returns a tuple with the two closest elements in the list, along with the distance between them. 

The function first sorts the list of numbers, then takes the first and second elements of the sorted list, and finally, calculates the Euclidean distance between the first and second elements.