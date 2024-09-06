```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize distance and closest variables
    distance = [float('inf')] * 2
    closest = [None]* 2
    # Sort the list based on the value of each number in the list
    numbers.sort(numbers)
    # Sort the list based on the value of each number in the list
    for index, number in enumerate(numbers):
        distance[index] = abs(number - float(numbers[index]))
        if closest[0] is None or closest[0] > distance[index]:
            closest[0] = distance[index]
    if closest[1] is None or closest[1] < distance[index]:
        closest[1] = distance[index]
    # Return the variables in the function
    return distance, closest
```
The function takes a list of numbers as an argument and returns a tuple of two floats, which are the two closest numbers to each other. The function sorts the the list based on the value of each number in the list, and then it initializes two variables: `distance` and `closest`. The function then compares the `distance` and `closest` variables and updates them accordingly. Finally, the function returns the two variables.