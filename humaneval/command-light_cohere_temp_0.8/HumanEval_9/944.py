```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until the given moment in the sequence.
    """
    list of integers -> List[int]
    """
    # Initialize the list with the first element only
    rolling_max_list = [numbers[0]]
    
    # Iterate over the list and add current element and max of the previous rolling list
    for num in numbers[1:]:
        rolling_max_list.append(num)
        max(rolling_max_list[:-1]) = rolling_max_list[-1]
        
    # Return the list
    return rolling_max_list

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This Python script defines a function called `rolling_max` that generates a list of the rolling maximum elements in a given list of integers. The `numbers` list is passed as an argument to the `rolling_max` function, and the function returns the resulting list, which contains the maximum element from the sequence at each moment. 

Example usage demonstrates how to call the `rolling_max` function with a sample list of numbers and print the output.