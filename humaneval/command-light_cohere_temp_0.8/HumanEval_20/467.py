Here is a self-contained Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    Returns a tuple containing the two closest elements.

    # Sort the sink to find the smallest and largest numbers in the list
    numbers.sort(numbers, reverse=True)
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    closest = (smallest, largest)
    return closest
```

This function takes a list of numbers as input and returns a tuple containing the two closest elements. The function first sorts the maximum and minimum numbers in the list. It then iterates through the numbers and compare them to the current minimum and maximum values. The number that is closer to the largest number will be assigned to the maximum value. The process continues until all numbers have been compared and assigned to their correct values.