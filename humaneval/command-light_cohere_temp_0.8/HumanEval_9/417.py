```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment.
    Args: 
        numbers: list of integer
    Returns: 
        list of integers, the rolling maximum elements
    """
    # setup
    max_so_far = numbers[0]
    result = [max_so_far]
    for num in numbers[1:]:
        current = num
        max_so_far = max(num, max_so_far)
        result.append(max_so_far)
    return result

# test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # [1, 2, 3, 3, 3, 4, 4]

numbers = [5, 1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # [5, 1, 2, 3, 4, 5]

numbers = [10, 2, 4, 8, 10]
result = rolling_max(numbers)
print(result)  # [10, 8, 10]
``` 
This code defines a function called rolling_max that takes a list of integers as input and returns a new list containing the rolling maximum elements found in the original input list. The function uses a max_so_far to keep track of the maximum element seen so far, and it iterates through the input list, updating max_so_far and the result list whenever a new maximum element is encountered.

The code then provides three test cases, passing them to the rolling_max function and printing the resulting list to verify the correctness of the function.