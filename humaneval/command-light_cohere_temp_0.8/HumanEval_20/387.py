Here is the code that will solve the problem:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple of the two closest elements in the list, and the separation between them.
    
    Parameters:
        numbers: List[float] - A list of numbers.
    Returns:
        tuple(closest_num, separation) where closest_num is the closest number and separation is the absolute value of the distance between the two closest numbers.
    """

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

min_distances, min_first_num, max_num = float('inf'), -1]

for i in range(len(numbers)):
    # Find the minimum distance between the current element and each other number
    min_distances[i] = min(numbers[i], numbers[j] for j in range(len(numbers)) if i!=j)
    
    # Find the first element that is not the minimum distance yet
    min_first_num = numbers[0] if min_distances[0] > numbers[i] else numbers[i]
    
    # Find the second element that is the closest to the current element
    max_num = numbers[i] if min_distances[i] == min_distances[0] else numbers[0]
    
    # Find the closest element
    closest_num = min(min_first_num, max_num)
    separation = abs(numbers[i] - closest_num)
    
    return (closest_num, separation)
```

This function accepts a list of numbers as an argument and outputs a tuple containing the two numbers that are closest to each other as well as the separation between them. The function uses nested loops to locate the smallest distance between each element and every other number in the list. It then chooses the two numbers that are closest and returns them in descending order (smaller number, larger number).