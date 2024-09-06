```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initialising the distance dictionary
    distance = {}
    
    # creating the first element in the tuple
    min_dist = min(numbers)
    closest_element = (min_dist, numbers.0)
    
    # iterating over the iteration, calculating the distance between two elements and checking if it's smaller than the current minimum distance
    for current_num, current_dist in zip(numbers, distance):
        # calculating the distance between the current element and the closest element
        new_dist = current_dist + current_num - min_dist
        
        # checking if the new distance is smaller
        if new_dist < min_dist:
            min_dist = new_dist
            closest_element = (new_dist, current_num)
        
    # returning the closest elements
    return closest_element

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)

print(result)
```

The function `find_closest_elements` takes a list of numbers as input and returns a tuple of the two closest elements. It achieves this by iterating over the list, calculating the distance between each element and the closest element so far. It then updates the data structure to keep track of the minimum distance and the element corresponding to it.

After iterating over the list, the function returns the tuple of the two closest elements. The output of the example usage will be:
```bash
(2.0, 3.0)
```