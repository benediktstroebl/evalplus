```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # Initialize variables to store the two closest elements and their relationship.
    closest1, diff = float('inf'), max_num = float('-inf')
    # Loop through the list
    for num in numbers:
        # Calculate the difference between the current number and the maximum number
        diff = num - max_num
        # Update the variables
        max_num = num
        closest = num
        # Check which pair of variables has the smallest difference
        if diff < closest + diff:
            closest, diff = num, diff
    # Return the closest elements in the original order
    return closest, diff
```
This function takes a list of numbers and returns a tuple containing the two closest elements, along with the difference between the two numbers. The function works by initializing variables to hold the closest element and the difference between the closest elements, respectively. The function then loops through the list, updating the variables based on the current element's value.