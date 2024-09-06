Here is a Python script that demonstrates the solution to the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize x and y variables
    x, y = 0, 1
    # Sort the numbers in ascending order
    sorted_numbers = [num for num in numbers if num not float('inf')] + [float('inf')]
    # Sort the two variables
    sorted_numbers.sort(sorted_numbers[::-1])
    # Return the two closest numbers in the x and y variables
    return sorted_numbers[x:2], sorted_numbers[y:2]
```

The above code uses the List[float] parameter to create a list of numbers, and the function **find_closest_elements** to return the two numbers that are the closest to each other. The code is a function is a great way to solve the problem of finding the closest pair of elements in a list of numbers.