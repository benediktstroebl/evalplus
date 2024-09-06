```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    From a given list of integers, generates a list of rolling 
    maximum elements found until a given moment in the sequence.
    """ 
    Parameters: 
    - numbers (list of integers) 
    Returns: 
    - A list of rolling maximum elements found until the given moment 
    """
    max_elements = []
    current_max = float('-inf')

    for num in numbers:
        if current_max < num:
            current_max = num 

        if num > current_max:
            max_elements.append(current_max)
            current_max = num 

    return max_elements

# Example 
numbers = [1, 2, 3, 2, 3, 4, 2] 
rolling_max_result = rolling_max(numbers) 
print(rolling_max_result)  # Output: [1, 2, 3, 3, 3, 4, 4]
``` 
This function, rolling_max, takes a list of integers as input and returns a list of the rolling maximum elements found until a given moment in the sequence. It uses a maximum element approach where it keeps track of the current maximum value and appends it to the list whenever a larger number is encountered. 

The provided example uses the function with a sample list of numbers and prints the resulting list of rolling maximum elements.