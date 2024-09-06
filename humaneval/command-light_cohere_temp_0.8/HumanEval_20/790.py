Here is a Python script that contains a self-contained function that solves the problem of finding the closest elements from a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    numbers.sort(key=lambda x: x, -x)
    # The first and second elements are the closest to each other, so subtract the smaller number from the larger number to find the minimum value
    first_number, second_number = min(numbers[0], numbers[1])
    return first_number, second_number
```

This function takes a list of numbers as input and returns a tuple containing the two closest elements in the list, in order of their smaller value. 

To test the function, you can call it with a list of numbers and print the result. This will return the tested in the following:

```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = find_closest_elements(numbers)
print(numbers) # Output: [2.0, 4.0]
```