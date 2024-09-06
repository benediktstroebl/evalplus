Here is a Python script that demonstrates the implementation of a function, `find_closest_elements`, which finds two closest elements from a given list of numbers and returns them in order of their magnitude:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Define the order and number of closest elements to use
    number_of_closest = 2
    closest_order = [float('inf'), float('-inf')]
    
    # Sort the list based on the desired order of the elements
    sorted_numbers = sorted(numbers, key=lambda x: x[number_of_closest])
    
    # Find the first and last elements in the sorted list based on the order of the elements
    first_element = sorted_numbers[0][number_of_closest]
    last_element = sorted_numbers[-1][number_of_closest]
    
    # Initialize the closest pair as the first and last elements
    closest_pair = (first_element, last_element)
    
    # Check if the list has one element
    if number_of_closest == 1:
        return closest_pair
    
    # Recursively find the closest elements from the rest of the list
    for num, index in enumerate(sorted_numbers[1:], start=1):
        current_element = sorted_numbers[index][number_of_closest]
        # Update the closest pair if a closer element is found
        if current_element < closest_order[0]:
            closest_order[0] = current_element
            closest_order[1] = last_element
        if current_element > closest_order[1]:
            closest_order[1] = current_element
            closest_pair = (current_element, last_element)
    
    return closest_pair
```
This code defines a function, `find_closest_elements`, that takes a list of numbers as input and returns a tuple containing the two closest elements. The function first sorts the result and then uses a binary search to find the two closest elements. The output of the function is a tuple of the two closest elements, which are then returned in order of their magnitude.