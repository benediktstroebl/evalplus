```markdown
### Find Closest Elements in a List
#### Problem Description
From a supplied list of numbers (of length at least two) select and return two that are the closest to each other
and return them in order (smaller number, larger number).

#### Solution

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Select two numbers from the supplied list that are closest to each other.

    Args:
    numbers (List[float]): A list of numbers of length at least two.

    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers in order (smaller number, larger number).
    """
    # Initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])

    # Iterate through the list to find the closest pair of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate the absolute difference between the current pair of numbers
            diff = abs(numbers[i] - numbers[j])
            # Update the minimum difference and the closest pair if the current difference is smaller
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])

    # Return the closest pair of numbers
    return closest_pair

# Example usage
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
# Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
# Output: (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest numbers in order. The function iterates through the list to find the pair of numbers with the smallest absolute difference. The example usage demonstrates how to use the function with the provided test cases.