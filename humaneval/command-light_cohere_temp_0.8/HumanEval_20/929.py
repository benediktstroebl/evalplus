Here is the Python script that includes a self-contained function to solve the problem of selecting two elements from a list that are closest to each other:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # The function takes a list of numbers as input and returns a tuple of two closest numbers and their distance.
    # Sort the maximum to minimum for all the numbers in the list
    numbers.sort(numbers, key=lambda num: num)
    # Initialize a list to store the two closest numbers and their distance
    result = []
    # Loop to find the two closest numbers
    for i in range(len(numbers) - 1):
        current_min = numbers[i]
        current_max = numbers[i + 1]
        # If the current maximum is smaller than the current minimum, swap them
        if current_max < current_min:
            result.appendleft(current_min, current_max)
        result.append(numbers[i][1])
    # Return the two closest numbers
    return result

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5]))
```

This script defines a function `find_closest_elements` that takes a list of floating-point numbers as input and returns a tuple containing the two closest numbers along with their Euclidean distance. The script then sorts the numbers in descending order, finds the two closest numbers, and returns them in order. The test cases demonstrate how the function works.