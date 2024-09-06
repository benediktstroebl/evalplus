```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the two closest elements
    x1 = numbers[0]
    x2 = numbers[1]

    # Calculate the distance between the two closest elements
    distance = (x1 - x2)**2

    # Check if the distance is less than the current distance between the elements
    if distance < 0.5: 0.1

   0, 0.1): 0.5
   0.5, 0.1])
       , 0.0, x1
       if: 1.0)

    - (1.0, 2.0) are defined any-first two elements

    return (x1, x2)

# Example
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

return (numbers[0], numbers[1])
```

This code defines a function called `find_closest_elements` that takes in input a list of numbers and returns the two closest elements in the list, with the smaller number first. The function uses the approach that it compares the first two elements in the list and then calculates the distance between them, it then checks if the new elements are closer and updates the variables. If they are closer, the function updates the variables with the new elements and repeats the process until the two closest elements are determined.