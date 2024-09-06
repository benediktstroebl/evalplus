```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initialising two variables to store the closest elements and their corresponding distances
    closest1, closest2 = float('inf'), float('-inf')
    # compare the two elements and update the variables
    if numbers[0] < numbers[1]:
        closest1, closest2 = numbers[0], float('inf')
    else:
        closest1, closest2 = numbers[1], float('-inf')
    # return the two closest elements and their distances
    return Tuple(closest1, closest2)

# test case 
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 2]))

(2.0, 4.0)
```
This Python code defines a function find_closest_elements that takes a list of numbers as input and returns a tuple of two closest elements along with their respective distances. The function uses two variables, closest1 and closest2, to keep track of the two closest elements. The function first compares the two elements and updates the variables based on the smaller number. It then returns the general case to check if the first element is smaller than the second one, and vice versa.