```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize closest and second variables
    closest = numbers[0]
    second = numbers[1]
    
    # Compare elements to find the closest and second
    for i in range(1, len(numbers)):
        if numbers[i] < closest:
            second = numbers[i]
        elif numbers[i] > closest:
            closest = numbers[i]
    
    # Return the two closest elements in the order of their positions
    return closest, second
```
This Python script defines a function find_closest_elements that takes a list of numbers as input and returns a tuple containing the two closest numbers in that list. The script uses the selection logic to find the two closest elements and return them in order, with the smaller number first. The function handles the testing by initializing the closest and second variables and then iterates through the list to find the closest elements. The returned result is a tuple of the two closest numbers, with the first element being the smaller number and the second element being the larger number.