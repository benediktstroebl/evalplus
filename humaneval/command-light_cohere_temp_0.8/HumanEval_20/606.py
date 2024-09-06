```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Define a tuple of the two closest elements and their corresponding distances.
    closest = (float('inf'), float('inf'))
    for i in range(len(numbers)):
        current = (numbers[i], i)
        for j in range(i+1, len(numbers)):
            current = (numbers[j], j)
            if current[0] < closest[0]:
                closest = current
    return closest

def test():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
   
    print(find_closest_elements(numbers)))
``` 

This script defines a function called find_closest_elements that takes a list of numbers and returns a tuple of the two closest elements and their corresponding distances. It initializes the the closest tuple with the infinity values. Then, it loops through all the numbers in the list and compares each number with the ones that come after it. If the current number is smaller than the closest one, it updates the closest tuple with the current number. Finally, it returns the closest tuple.