```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements found in the sequence until a given moment.
    Return a maximum elements in descending order.
    """
    time is using a list of integers, generates a list of rolling max elements found until a given moment 
    in the sequence.
    """
    elements in descending order.
    """ 

    time complexity O(n).
    """
    # Initialize a list of numbers and a counter
    max_elements = [0]
    count = 0
    # Generate a list of rolling max elements found until a given moment in the sequence
    while count < len(numbers):
            current = numbers[count]
            # Update the max element in the list
            max_elements[0] = max(max_elements[0], current)
            # increment counter
            count += 1
    return max_elements

# Test cases
test_cases = [1, 2, 3, 4, 5, 6]
test_results = rolling_max(test_cases)
print(test_results)
```

The function 'rolling_max' takes a list of integers as input and returns a list of integers, representing the maximum element in each iteration of the list until the given moment is reached. The time complexity of the code is O(n), where n is the length of the input list.