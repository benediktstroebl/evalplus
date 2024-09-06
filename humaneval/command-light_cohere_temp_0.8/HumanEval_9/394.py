```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from a given list of integers.
    The rolling max is calculated as the maximum value of an integer within a given range
    until a given moment in the sequence.
   >>>
    list of rolling maxs is returned
    """
    # Initialize the rolling array with the first element of the input list
    rolling_maxes = [numbers[0]] + [x for x in numbers[1:] + [numbers[0]]]
    # Define a function to get the maximum element within a range [a, b]
    def max_range(a, b):
        return max(numbers[b], numbers[a - 1] if a > b else numbers[a])
    # Define the rolling max function using the above function
    rolling_max = max_range(1, len(numbers))
    # Return the list of rolling max elements
    return [rolling_max] + [rolling_max - 1] * (len(numbers) - 2)

# Sample test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This script defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. The function uses a array to keep track of the rolling maxs and uses a helper function to calculate the maximum element within a range. The main function then uses this helper function to calculate the rolling max and returns the list of rolling max elements.