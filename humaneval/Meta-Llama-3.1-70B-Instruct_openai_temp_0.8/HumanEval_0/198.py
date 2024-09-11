```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Create a set from the list to remove duplicates and improve lookup efficiency
    num_set = set(numbers)
    
    # Iterate over each number in the set
    for num in num_set:
        # Check all numbers in a range slightly larger than the threshold
        for i in range(int(num - threshold * 100), int(num + threshold * 100) + 1):
            # Convert the integer back to a float and check if it's in the set
            check_num = i / 100.0
            if check_num in num_set and check_num!= num and abs(num - check_num) < threshold:
                return True
                
    # If no close elements are found, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

### Explanation:
- We create a set from the input list to remove duplicates, which improves lookup efficiency.
- Then, we iterate over each number in the set.
- For each number, we check all numbers in a range slightly larger than the threshold.
- We convert the integer back to a float and check if it's in the set.
- If we find a number that's within the threshold and not the same as the current number, we return True.
- If we don't find any close elements after checking all numbers, we return False.

### Note:
- The above solution has a time complexity of O(n*m) where n is the number of elements in the list and m is the range of the threshold.
- It may not be efficient for large lists or small thresholds. There are more efficient algorithms available, such as using a binary search tree or a sweep line algorithm, but they are also more complex to implement.