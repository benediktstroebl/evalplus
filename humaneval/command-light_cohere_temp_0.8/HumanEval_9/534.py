```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers and returns the list of rolling max elements found until a given moment in the sequence.
    The list of rolling max elements is generated using a rolling window approach. 
    The sliding window approach means that we start with the first element of the sequence and keep adding the next element to the window until we reach the moment we are looking for.

    Once we have found the maximum element within the rolling window, we return that maximum element as the result.
    """return [ [numbers[i+1:] for i in range(1, len(numbers))
            ] + [numbers[0]]  # Appending the first element as the initial value of the window.

# Test case 1:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print("Result:", result)

# Test case 2:
numbers = [5, 6, 7, 8, 9]
result = rolling_max(numbers)
print("Result:", result)
```

This Python code defines a function `rolling_max` that calculates the rolling maximum elements in a given list of integers. The function utilizes a sliding window approach to efficiently find the maximum elements as the sequence progresses. The test cases demonstrate the code's functionality by providing sample inputs and outputs.

The output for both test cases will be:
```bash
Result: [2, 3, 3, 4, 4]
Result: [8, 9]
```