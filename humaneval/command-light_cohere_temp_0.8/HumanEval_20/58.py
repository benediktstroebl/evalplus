Here is a Python script that solves the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple containing the two closest numbers from the list, along with their order.

    If the list is empty, return (None, None).
    """
    if not numbers:
        return (None, None)

    numbers.sort()
    closest_first, closest_second = (float('inf'), -float('inf'))
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            # Calculate the squared distance between the two numbers
            squared_distance = (numbers[i] - numbers[j]) ** 2

            # If this squared distance is smaller than the current closest pair, update the closest pair
            if squared_distance < closest_first[0] * closest_first[1]:
                closest_first = (numbers[i], closest_first[0] + squared_distance / closest_first[1])
                closest_second = (numbers[j], closest_first[0] + squared_distance / closest_first[1])

            # If this squared distance is smaller than the current closest pair, update both the first and second closest pairs
            elif squared_distance < closest_second[0] * closest_second[1]:
                closest_second = (numbers[i], closest_second[0] + squared_distance / closest_second[1])

    return closest_first, closest_second
```

This function can be used to solve the problem of finding the closest pairs of numbers in a given list. The function takes a list of numbers as input and returns a tuple containing the two closest numbers from the list, along with their order (smaller number, larger number).  The function uses the `sort()` function to sort the list of numbers in ascending order before finding the closest pairs.