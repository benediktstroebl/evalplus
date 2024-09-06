Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the numbers in ascending order
    numbers.sort(numbers)
    # Initialize a tuple with two closest numbers
    closest = Tuple(numbers[0] , numbers[1])
    # Check if the two elements in the tuple are the same
    if numbers[0] == numbers[1]:
        closest = Tuple(numbers[0], numbers[0])
    return closest
```

This code defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements in the list, with the smallest number first. 

It sorts the list of numbers in ascending order and uses the tuple unpacking feature to create a tuple with the two closest numbers.  The tuple is assigned to the variable `closest`. 

Then, it checks if the two elements in the tuple are the same and if not, it assigns the tuple with the same element to the `closest` variable, effectively replacing the first element with the second one. 

Finally, it returns the `closest` tuple, which contains the two closest elements in the list.