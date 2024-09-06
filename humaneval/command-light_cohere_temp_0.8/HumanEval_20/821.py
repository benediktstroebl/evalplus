```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize distances and indices.
    distances = [ n for n in numbers ]
    indices = list(range(len(numbers)))
    # Sort the indices based on the corresponding distance
    indices.sort_keys(distances)
    # Extract the first and second index of the sorted list
    first_index, second_index = indices[0], indices[1]
    # Reconstruct the two closest numbers based on the sorted indices
    first_number = numbers[first_index]
    second_number = numbers[second_index]
    return first_number, second_number
```
The above Python function, "find_closest_elements," takes a list of numbers as input and returns a tuple containing the two closest numbers from the list, along with their relative order. It uses the set to sort the indices of the input list based on their corresponding distances and then reconstructs the two closest numbers from the sorted list. 

This function can be used to quickly find the closest pairs of elements in a given list, which can be useful in various applications such as data analysis, machine learning, and so on.