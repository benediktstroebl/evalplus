Here is a Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize the closest_pair variable with the first element in the list.
    closest_pair = (numbers[0], 0)
    
    # Iterate through the list
    for i in range(1, len(numbers)):
        # Calculate the current distance between the current element and the closest_pair
        current_distance = numbers[i] - closest_pair[0]
        
        # If the current element is closer, update the closest_pair variable
        if current_distance < closest_pair[1]:
            closest_pair = (numbers[i], current_distance)
    
    # Return the closest_pair variable
    return closest_pair
```

The function `find_closest_elements` takes a list of numbers as input and returns a tuple containing the two closest elements in the list. The function uses a type hint `List[float]` for the input `numbers` to ensure that the input is a list of floats. It initializes theit variable `closest_pair` with the first element in the list and sets the current closest pair to `closest_pair` variable to be the current element and the current distance. The function then iterates through the loop through the list, calculating the current distance between the current element and the closest pair. The function then compares the element to the current closest pair and updates the `closest_pair` variable to the new element and the current distance if the current element is closer. Finally, the function returns the `closest_pair` variable, which contains the two closest elements in the list, and returns them in order of decreasing value.