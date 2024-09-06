```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements from the list that are the closest to each other and returns them in order (smaller number, larger number).
    Get a list of numbers, the function selects two elements from the list that are the closest to each other according to the provided metric (in this case, the Euclidean distance between the numbers).
    """
    numbers = sorted(numbers)  # Sort the list in ascending order
    smallest_index = 0
    largest_index = len(numbers) - 1
    while smallest_index <= largest_index:
        current_element = numbers[smallest_index]
        next_element = numbers[largest_index]
        largest_index -= 1
        smallest_index += 1
        if current_element < next_element:
            closest_pair = (current_element, next_element)
            return closest_pair
    return None

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

find_closest_elements(numbers)
```
This code defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements in the list. The function works by sorting the input list, finding the smallest and largest elements, and then iteratively selecting the elements that are closer to each other until a valid closest pair is found.