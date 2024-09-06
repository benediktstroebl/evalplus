```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the numbers in ascending order
    numbers.sort(numbers)
    # Get the two closest numbers and return them in the order of decreasing value
    # smaller number first
    smallest_number, largest_number = numbers[0], numbers[-1]
    while numbers[1] != numbers[0] and numbers[1] != numbers[-1]:
        smallest_number, largest_number = numbers[1], numbers[0]
    return smallest_number, largest_number

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print_closest_elements(numbers)
```
The function `find_closest_elements` takes a list of numbers as input and returns a tuple with the two closest elements in descending order. It uses a sorting algorithm to sort the list of numbers in ascending order and then iterates through the list, continuously swapping the elements with the smallest and largest values. It uses the swapping logic to find the two closest elements and returns them in the correct order.