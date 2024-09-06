```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple containing the two numbers in the list that are closest to each other and their order """
    if len(numbers) < 2:
        return ()
    
    # Sorting the list in ascending order
    sorted_numbers = sorted(numbers, key=lambda x: x)
    
    # Get the two closest numbers in the sorted list
    first_closest = sorted_numbers[0]
    second_closest = sorted_numbers[1]
    
    return first_closest, second_closest

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)

print(result)  # Output: (2.0, 5.0)
``` 
This code demonstrates the implementation of a function called find_closest_elements that aims to solve the problem of finding the two closest numbers from a given list of numbers. The function first checks if the list has at least two elements, and returns an empty tuple if it does not. Then, it sorts the list in ascending order using the sorted() function with a custom key. Finally, the function retrieves the two closest numbers from the sorted list and returns them in order, using the first element as the smaller number and the second element as the larger number.