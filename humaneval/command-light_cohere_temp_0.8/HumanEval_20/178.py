```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first element of the tuple
    closest1 = numbers[0]
    
    # Initialize the second element of the tuple
    closest2 = numbers[1]
    
    # Keep finding the next smallest number until we reach the end of the list
    for num in numbers[2:]:
        # Compare current number with the current closest numbers
        if num < closest1:
            closest1 = num
        elif num < closest2:
            closest2 = num
    
    # Return the two closest numbers
    return closest1, closest2
```
This code uses the List and Tuple data types from the typing module to create a function that finds the closest elements to each other in a list of numbers and returns them in order. It uses a maximum time list of numbers and creates two variables, closest1 and closest2, to keep track of the two closest elements. The function then loops through the list of numbers, finds the next smallest number, and compares it with the current closest elements. Finally, it returns the pair of the smallest number and the larger number as the result.