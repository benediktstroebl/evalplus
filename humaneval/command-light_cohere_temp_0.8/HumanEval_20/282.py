Here is a Python script that defines a self-contained function that solves the problem of finding the closest elements from a list of numbers:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # sort the list of numbers
    numbers.sort(lambda x: x<1.0)

    smallest = float('inf')
    # return the largest number in the list
    return (numbers[0], numbers[1])
```
This function takes a list of numbers as input and returns a tuple containing the two closest elements from the list, in ascending order. The function sorts the list of numbers using a lambda function to sort the list such that the smallest number is first. This ensures that the closest elements will be returned first.