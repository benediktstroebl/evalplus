Here's a self-contained Python function that solves the problem of finding the closest elements from a supplied list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    numbers.sort(numbers)

    # Initialize variables to track the minimum and maximum values, as well as the current element
    min_val, max_val, current_element = numbers[0], numbers[0]

    # Loop through the list
    for num in numbers[1:]:
        # Update the current element and min/max values
        current_element = num
        min_val = num
        max_val = num

        # Return the current element and its value
        return current_element, min_val
```
This function takes a list of numbers as input and returns a tuple containing the current element in the list and its corresponding minimum value. The function works by first sorting the list of numbers in ascending order. Then, it initializes variables to track the minimum and maximum values, as well as the current element. The function then loops through the list, updating the current element and min/max values at each step. Finally, the function returns the minimum and maximum values, as well as the current element, and returns the tuple containing the current element and its value.