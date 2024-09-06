```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns the two elements of the list that are the closest to each other and returns them in order (smaller number, larger number).
    numbers = [1.0, 2.0, 3.0, 4]
   0, 5]
    # Sort the list of numbers
    numbers.sort()

   
   , reverse = True
    # Get the two closest elements
    x1 = numbers[0]
    x2 = numbers[1]
    # Compare the two elements
    if x1 == x2:
        closest_element = x1
    elif x1 < x2:
        closest_element = x1
        other_element = x2
    else:
        closest_element = x2
        other_element = x1
    # Return the two closest elements
    return Tuple(closest_element, other_element)

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5]))
``` 
This Python code defines a function called `find_closest_elements` that takes a list of floating-point numbers as input and returns a tuple containing the two elements in the list that are the closest to each other. The function uses the sorting the list of numbers and then compares the two closest elements to determine which is the "closest element" and the "other element". Then, the function returns the two elements in that order. 

Finally, the function is tested with a list of numbers and the result is printed.