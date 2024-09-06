Here is a Python script that solves the problem of finding the two closest elements from a supplied list of numbers, and passes the result as a tuple:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Get the first and second elements from the sorted list
    first_element = sorted_numbers[0]
    second_element = sorted_numbers[1]
    
    # Check the relative difference between the two elements
    if first_element - second_element > 0:
        return first_element, second_element
    else:
        return second_element, first_element

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 2]
return find_closest_elements(numbers)
```

This function takes a list of numbers as input and returns a tuple containing the two closest elements in order of magnitude. The function first sorts the array of numbers and then retrieves the first and second elements using the sorted index values. Then, it checks if the difference between the first and second element is greater than 0. If so, it returns the first element and second element. If not, it returns the second element and first element.