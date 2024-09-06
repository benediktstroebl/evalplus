```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Find two numbers that are closest to each other in the list.
   
    closest1 = float('inf')
    second_closest = float('-inf')
    for i in range(len(numbers)):
        # Calculate the difference between the numbers and the current closest pair
        diff = numbers[i] - closest1
        if diff < second_closest:
            closest1 = numbers[i]
            second_closest = diff
    # Return the two closest numbers in order
    return (closest1, second_closest)

>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2])
``` 
``` 
Do you require any additional assistance related to Python scripting or other AI topics?