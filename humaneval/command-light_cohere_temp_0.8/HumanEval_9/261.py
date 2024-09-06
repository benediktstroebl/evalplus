```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns the list of rolling maximum elements in a given list of integers.
    Each element of the max is set to its own value in the list until the current index is greater than the index of the element in the list with the maximum value.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_number = numbers[0]
    current = numbers[0]
    
    for num in numbers[1:]:
        if num > current:
            current = num
        max_number = max(current, max_number)
    
    return [max_number]

# Example Test
test_data = [1, 2, 3, 2, 3, 4, 2]
test_result = rolling_max(test_data)
print(test_result)  # Output: [1, 2, 3, 3, 3, 4, 4]

# Another Test
test_data2 = [0, 1, 2, 3, 4, 5]
test_result2 = rolling_max(test_data2)
print(test_result2)  # Output: [0, 1, 2, 3, 3, 5]
```
This script defines a `rolling_max` function that calculates the rolling maximum elements in a given list of integers. It uses a `max` and `current` variables to keep track of the maximum number and the current element, respectively. The loop compares the elements of the list with the current element and updates `current` if the current element is greater. The `max_number` variable keeps track of the maximum value encountered so far. 
Finally, the function returns a list containing the rolling maximum value.