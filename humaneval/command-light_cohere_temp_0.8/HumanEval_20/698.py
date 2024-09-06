Here is a Python script that is self-contained and can solve the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Select two elements that are the closest to each other
    x1, y1 = min(numbers[0] , numbers[1]), max(numbers[0] , numbers[1])
    a, b = (numbers[0] - x1) , (numbers[1] - y1)
    return (a, b)

def test():
    numbers = [1.0, 2.0, 3.0, 4, 5.0, 2]
    a = find_closest_elements(numbers)
    assert (a, b) == (2.0, 3.0) #
     same program
print('Test passed!
```
This script defines a function `find_closest_elements` that takes in a list of numbers and returns a tuple of the two closest numbers. It then defines a test function that takes in the `find_closest_elements` function and tests if it works correctly with a sample list of numbers.

The test function will print out 'Test passed' if the test passes.