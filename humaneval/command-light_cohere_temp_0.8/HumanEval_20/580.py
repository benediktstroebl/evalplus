```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    from typing import List, Tuple
    """
    # Initialize variables
    l_min, r_max = float('inf'), float('-inf')
    closest = None, second_closest = None

    # Loop through list of numbers
    for num in numbers:
        # Calculate the difference between current and next closest elements
        diff = abs(num - closest)

        # If difference is less than the current maximum difference, update the closest element
        if diff < l_min:
            closest = num
            l_min = diff

        # If difference is greater than the current minimum difference, update the second closest element
        elif diff > r_max:
            second_closest = num
            r_max = diff

    # Return the two closest elements and their relative order
    return closest, second_closest
``` 
This script defines a function, `find_closest_elements`, which accepts a list of floating-point numbers as input and outputs a tuple of the two closest elements as well as the relative order of those elements. The function uses a process to identify the two closest elements in the input list based on the differences between each pair of adjacent elements. The function initializes two variables, `l_min` and `r_max`, to keep track of the smallest and largest differences encountered so far. 

It then loops through the input list of numbers, comparing each number to the current `closest` element to determine the smallest difference. If this difference is less than the current `l_min`, the `closest` element is updated to the current number. Similarly, if this difference is greater than the current `r_max`, the `second_closest` element is updated to the current number. After the loop, the function returns the two closest elements along with their relative order.