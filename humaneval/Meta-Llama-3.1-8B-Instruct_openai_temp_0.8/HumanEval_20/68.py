Here's a Python script that solves the problem.

```markdown
# Python Script: Find Closest Elements

## Problem Statement
From a supplied list of numbers (of length at least two) select and return two that are the closest to each other 
and return them in order (smaller number, larger number).

## Solution

### Code

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find two numbers in a list that are the closest to each other.

    Args:
    numbers (List[float]): A list of numbers of length at least two.

    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers in order (smaller number, larger number).
    """
    
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize with the smallest number
    
    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current and next numbers
        diff = abs(numbers[i] - numbers[i + 1])
        
        # If the current difference is smaller than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

### Example Usage

if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
    print(find_closest_elements(numbers))  # Output: (2.0, 2.2)
    
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
    print(find_closest_elements(numbers))  # Output: (2.0, 2.0)
```

### Explanation

This script uses a simple sorting-based approach to find the closest pair of numbers in the list. First, it sorts the list in ascending order. Then, it iterates over the sorted list to find the pair of numbers with the smallest absolute difference. This is done by keeping track of the minimum difference found so far (`min_diff`) and updating it whenever a smaller difference is found. The pair of numbers corresponding to the smallest difference is stored in the `closest_pair` variable. Finally, the script returns the `closest_pair` as a tuple.

This solution has a time complexity of O(n log n) due to the sorting step, where n is the length of the input list. The subsequent iteration over the sorted list has a time complexity of O(n), but it does not affect the overall time complexity because it runs after the sorting step.