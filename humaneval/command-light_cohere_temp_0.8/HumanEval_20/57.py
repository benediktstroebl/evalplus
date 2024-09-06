```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Use the Pythagorean distance formula to calculate the distance between two elements in the list
    # Sort the list by the calculated distance in descending order
    # Return the two elements that are the closest to each other, and sort them in ascending order (smaller number, larger number)
    # Return the two elements in order of increasing value
    return (numbers[0], numbers[-1]), sorted([numbers[0], numbers[-1]])

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]

numbers = sorted([numbers, numbers[::-1]], key=lambda x: x[1] - x[0]))

print(find_closest_elements(numbers))
```