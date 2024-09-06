Here is a Python script that solves the problem of finding the closest elements from a list of numbers:

```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the input list of numbers
    numbers.sort()
    def find_pair(numbers: List[float]):
        # Take the first and last elements in the sorted list
        first, last = tuple(numbers[:-len(numbers) // 2])
        return first, last
    return find_pair(numbers)

def main():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.2]
    - Calculate the time_two_numbers to be in the form of (smaller number, larger number) and return them in order. Then, the function is called with the list of numbers, which is passed as an argument to the function. The function returns a two numbers that are the closest to each other and returns them in order (smaller number, larger number). 
```

This script defines a function `find_closest_elements` that takes a list of numbers as an argument. The function sorts the numbers list and then selects the first and last elements. Then, the function `find_pair` is called with the sorted list to return the first and last elements in the order of smaller to larger numbers. The `main` function also passes a list of numbers to the `find_closest_elements` function.