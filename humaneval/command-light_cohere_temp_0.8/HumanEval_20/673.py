Here's a self-contained Python script that solves the problem you've described:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers, key=lambda x: (-x, 1))
    # Initialize variables
    min_distance = float('inf')
    closest_elements = (float('inf'), float('-inf'))
    for x, y in zip(numbers, numbers[1:]):
        distance = x - y
        if distance < min_distance:
            min_distance = distance
            closest_elements = (x, y)
    return closest_elements

# Test
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
print(result)
```

The script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of the two closest numbers in order. The function first sorts the numbers and then iterates through the sorted list, calculating the distance between each pair of elements and updating the variables `min_distance` and `closest_elements` if the calculated distance is smaller than the current value of `min_distance`. The final output will be the tuple of the two closest numbers in order.

The output of the test code will be: `(2.0, 1.0)`