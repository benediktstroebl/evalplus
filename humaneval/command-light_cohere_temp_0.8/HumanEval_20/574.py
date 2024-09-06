Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # sort the list of numbers
    numbers.sort(key=lambda x: x)

    # select two numbers that are the closest to each other
    first, second = numbers[0], numbers[-1]
    while numbers[1] - numbers[0] > numbers[1] - second:
        first, second = numbers[1], numbers[0]
    return first, second
```
This function takes a list of numbers as input and returns a tuple of the two closest numbers. The function sorts the `numbers` in ascending order and then uses a while loop to continually switch the `first` and `second` variables until the difference between `numbers[1]` and `numbers[0]` is less than the difference between `numbers[1]` and `second`. 
This will ensure that the two closest numbers are always the first and last numbers in the sorted list.