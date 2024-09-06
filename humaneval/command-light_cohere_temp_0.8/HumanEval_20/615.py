```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initial sorting of numbers
    numbers.sort(numbers) = sorted(numbers, reverse=True)
    # Find the two closest elements
    i = 0
    j = len(numbers) - 1
    while i < j:
        current_distance = (numbers[i] + numbers[j]) / 2
        next_distance = numbers[i] + numbers[j]
        if current_distance < next_distance:
            i += 1
        else:
            j -= 1
    # Return the two closest elements
    return (numbers[i], numbers[j])

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
```
This script defines a function `find_closest_elements` that takes a list of numbers and returns a tuple of the two closest elements in the list. The function first sorts the numbers in descending order and then iterates through the list to find the two closest elements.  The result returns the pair, with the smaller number first.