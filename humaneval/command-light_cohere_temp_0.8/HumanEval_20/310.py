Here is a Python script that solves the problem of finding the two closest elements from a list of numbers:
```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # Define the minimum and maximum values for each element
    min_val = min(numbers)
    max_val = max(numbers)
    # Define the closest element indices
    closest_index = 0
    while True:
        current_val = numbers[closest_index]
        if current_val > max_val or current_val < min_val:
            break
        # Swap the closest element with the other element
        numbers[closest_index], numbers[1-closest_index] = numbers[1-closest_index], numbers[closest_index]
        # Move the indices to the next two elements
        closest_index = 1 + closest_index
    return (numbers[closest_index], numbers[1-closest_index])
```
This function takes a list of numbers as input and returns a tuple containing the two closest elements in the list. The function uses the two variables, min_val and max_val, to store the minimum and maximum values for each element in the list. The function also uses a closest_index variable to keep track of the index of the closest element found so far. The function uses a strategy of swapping the elements to get the correct order of the closest elements. Finally, the function returns the tuple containing the two closest elements in the correct order.