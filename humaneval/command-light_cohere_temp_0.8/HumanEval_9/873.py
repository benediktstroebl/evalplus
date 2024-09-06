Here's the code with comments explaining each section:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers as input and returns a list of rolling maximum elements found
    until a given moment in the sequence.
    The function uses the particular sequence of maximum elements to determine which
    one to show in the output.
    """
    list of rolling max elements is returned.
    """ The important list of numbers, the function starts with the first element and 
    rolls it forward, keeping track of the maximum element seen so far.
    """
    list of rolling max elements will have the same length as the input list, 
    but with the maximum element of each moment in the sequence.
    """ numbers: List[int]
    return_list: List[int]
    """
    return_list = []  # List to store the rolling maximum elements
    for num in numbers:  # Loop through each number in the input list
        current_max = num  # Current maximum element
        seen_so_far = [num]  # List of elements seen so far
        for other in seen_so_far:  # Loop through the elements seen so far
            if other > current_max:  # If the current element is larger than the previous
                current_max = other  # Set the current maximum to the previous max
            seen_so_far.append(other)  # Update the list of rolling max elements
        return_list  # Return the list of rolling max elements
```
This function takes a list of integers and returns a list of integers that represent the maximum element from the sequence at each moment. The function uses a max element found at the current position to determine which one to show in the output.

The function uses the rolling technique, where the current element is compared with the previous ones to find the maximum element. The sequence of maximum elements is determined using the current element, and the elements that have been seen so far. The rolling max elements are the same length as the input list, with the maximum element of each moment in the sequence.