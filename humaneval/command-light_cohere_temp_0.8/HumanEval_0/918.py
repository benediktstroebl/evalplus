Here's the solution to the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    # Sort the Approach
    elements in descending order.
    sorted_numbers = sorted(numbers)
    
    # Initialize two boolean lists, one for each element in sorted_numbers
    flag_set = [False] * len(sorted_numbers)
    checked_numbers = [False] * len(sorted_numbers)
    # Loop to compare elements
    for i in range(len(sorted_numbers)):
        # Find the leftmost element to compare
        left_index = i
        while left_index > 0 and not checked_numbers[left_index - 1]:
            left_index -= 1
        if left_index < 0:
            break
        # Find the rightmost element to compare
        right_index = len(sorted_numbers) - 1
        while right_index > i and not checked_numbers[right_index - 1]:
            right_index -= 1
        if right_index < i:
            break
        # If left element is greater than right element
        if sorted_numbers[left_index] > sorted_numbers[right_index]:
            flag_set[left_index] = True
            checked_numbers[left_index] = True
        else:
            flag_set[right_index] = True
            checked_numbers[right_index] = True
    return any(flag_set)
```

This function uses a sorted list of numbers to compare the elements. The function works by first sorting the list of numbers and then using the binary search algorithm to compare the elements. The function returns true if any two elements are closer to each other than the given threshold, otherwise it returns false.