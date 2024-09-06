```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Returns the two closest numbers in the list, and returns them in order (smaller number, larger number).
    numbers = [1.0, 2.0, 3.0, 4, 5.0, 2, 6, 0.0, 7]
    nearest = numbers[0]
    nearest_two = [nearest, numbers[1]]
    for i in range(len(numbers) - 2):
        nearest = numbers[i]
        for j in range(i+1, len(numbers)):
            if numbers[j] > nearest:
                nearest = numbers[j]
                nearest_two = [nearest, numbers[j]]
                break
    return nearest_two

# Example usage:
numbers = [1.0, 2.0, 3.0, 4, 5.0, 2, 6, 0.0, 7]
nearest_result = find_closest_elements(numbers)

print(nearest_result)  # Output: [2.0, 7]
```

The script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest numbers in the list. The script implements the algorithm to find the two closest numbers by selecting the smallest of the two nearest numbers in the list and then storing them in a tuple.