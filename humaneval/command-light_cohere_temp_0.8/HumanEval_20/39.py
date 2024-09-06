```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Initialize variables
    min_number = float('inf')
    max_number = float('-inf')
    closest_pair = (None, None)
    
    # Loop to find the closest elements
    for i in range(len(numbers)):
        current_number = numbers[i]
        
        # Update variables
        min_number = min(min_number, current_number)
        max_number = max(max_number, current_number)
        
        # Check if a new closest pair was found
        if current_number is not None:
            closest_pair = (current_number, i)
    
    # Return the closest pair
    return closest_pair

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = find_closest_elements(numbers)

```
This function called `find_closest_elements` takes in a list of numbers and returns a tuple of the two numbers that are closest to each other. The function first sorts the numbers list in ascending order. Then, it initializes a few variables: `min_number` and `max_number` to store the minimum and maximum numbers in the list respectively. The `closest_pair` variable is initialized to `None` to represent that no closest pair has been found yet. 

The function then enters a loop that iterates over the sorted numbers list. For each number in the list, the current number is assigned to the variable `current_number`. 

Inside the loop, the function updates the `min_number` and `max_number` to be the minimum and maximum of the current number and the current number. The `closest_pair` variable is checked to see if the current number is not `None`, indicating that a new closest pair was found. If a, the variable `closest_pair` is updated to store the current number as the first number in the pair and the index of the pair.

Finally, the function returns the `closest_pair` variable, which contains the two numbers that are closest to each other in the list.