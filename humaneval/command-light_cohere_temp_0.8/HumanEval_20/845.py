Here is a Python script that solves the problem of finding the closest elements in a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Take the two closest numbers and return them in order
    return numbers[0:1]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
numbers = find_closest_elements(numbers)
```

In this script, the function `find_closest_elements` takes a list of numbers and returns a tuple containing the two numbers that are the closest to each other. The function uses the sorting method to sort the list of numbers, and then returns the two closest numbers in order.

The example usage at the bottom demonstrates how to call the function with a list of numbers and store the returned tuple in a variable.