```markdown
### Rolling Maximum Elements in a List

This script generates a list of rolling maximum elements found until a given moment in the sequence.

#### Code

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximum elements
    max_elements = []
    
    # Initialize the maximum element as negative infinity
    max_so_far = float('-inf')
    
    # Iterate over each number in the input list
    for num in numbers:
        # If the current number is greater than the maximum so far, update the maximum
        if num > max_so_far:
            max_so_far = num
        
        # Append the maximum so far to the list of max elements
        max_elements.append(max_so_far)
    
    # Return the list of rolling maximum elements
    return max_elements

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

#### Explanation

This script uses a simple iterative approach to find the rolling maximum elements. It initializes an empty list to store the maximum elements and a variable `max_so_far` to keep track of the maximum element seen so far. It then iterates over each number in the input list, updating `max_so_far` if a larger number is found and appending `max_so_far` to the list of max elements after each iteration. The list of max elements is returned at the end.

This solution has a time complexity of O(n), where n is the length of the input list, making it efficient for large inputs.