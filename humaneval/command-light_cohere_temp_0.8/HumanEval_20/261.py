```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize closest and second closest elements.
    closest = float('inf')
    second_closest = float('-inf')

    # Sort the list of numbers.
    numbers.sort()

    particular order in descending order.
    # Set the1 the2 closest element and second closest element.
    element1 = numbers[0]
    element2 = numbers[1]

    # Check if the current element is the closest element.
    if element <= closest:
        closest = element
    element = element1
    element1 = element

    # Check if the current element is the second closest element.
    if element2 <= second_closest:
        second_closest = element

    return closest, second_closest

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(find_closest_elements(numbers))
```

The function `find_closest_elements` takes a list of numbers as input and returns a tuple containing the two elements that are closest to each other. The function first sorts the list of numbers in descending order and then initializes the `closest` and `second_closest` variables to a large and negative infinity value, respectively. After sorting the list, the function checks if the current element is the closest element, and if not, it updates the `closest` variable to the current element.

The function also checks if the current element is the second closest element, and if so, it updates the `second_closest` variable to the current element. The function then returns the closest and second closest elements.

The provided example usage demonstrates how to call the `find_closest_elements` function with a list of numbers and print the returned tuple.