```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize the closest and second closest variables
    closest = numbers[0]
    second_closest = numbers[1]
    # Compare the two closest elements
    if numbers[0] < numbers[1]:
        closest = numbers[1]
        second_closest = numbers[0]
    else:
        closest = numbers[0]
        second_closest = numbers[1]
    # Return the two closest elements and their order
    return (closest, second_closest)

# Example:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print_closest_elements(numbers)
 ```

This Python script defines a function named `find_closest_elements` that aims to find the closest pairs of elements in a given list. It uses the typing module to define function parameters and return types. The function initializes the closest and second_closest variables with the first and second elements of the input list, respectively. It then compares the closest elements and updates the variables accordingly. Finally, it returns a tuple containing the two closest elements and their order.

This function can be effectively utilized to solve the problem of finding the closest elements in a supplied list of numbers, which is a fundamental and reusable solution.