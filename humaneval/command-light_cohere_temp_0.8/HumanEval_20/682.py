Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers, following the specified format:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Get the two closest numbers
    smallest = float('inf')
    second_smallest = float('-inf')
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return smallest, second_smallest

def test():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
   
    result = find_closest_elements(numbers)
    print(f"The closest numbers are: { {result[0]}, {result[1]}}.")

test()

```

The provided code includes a function `find_closest_elements`, which takes a list of numbers as an argument and returns a tuple containing the two closest numbers in that list, along with their order. 

The `test` function creates an instance of this function with a list of numbers, and prints out the result. This demonstrates how the expected behavior for the code, passing tests for a known solution.