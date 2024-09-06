Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the first and second closest element variables
    first_closest, second_closest = (sorted_numbers[0], sorted_numbers[1])
    
    # Loop through the list and find the current closest pair
    for i in range(2, len(sorted_numbers)):
        current_pair = (sorted_numbers[i], sorted_numbers[i+1])
        if current_pair < first_closest + second_closest:
            first_closest, second_closest = current_pair
    
    return first_closest, second_closest

```

This function takes a list of numbers as input and returns a tuple containing the two numbers that are the closest to each other. It does this by sorting the list of numbers in ascending order, and then initializing the first and second closest elements to be the first and second elements of the sorted list, respectively. After that, it loops through the list and finds the current closest pair. The current pair is checked to see if it is smaller than the first and second closest elements combined. If the current pair is indeed smaller, it is replaced with the pair.

The function returns the first and second closest elements, which are stored in the `first_closest` and `second_closest` variables.