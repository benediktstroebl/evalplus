Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Initialize a set to hold the first and last elements of the list
    set1, set2 = set([numbers[0]], [numbers[-1]])

    # Iterate over the list and check if the two elements at the current index are closer than the threshold
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + threshold < numbers[j] or numbers[i] - threshold > numbers[j]:
                set1.add(numbers[i], numbers[j])
                set2.add(numbers[i], numbers[j])

    # If the set has no common elements with set2, then the numbers are not close enough
    return len(set1) == len(set2)

# Test the function
numbers = [1.0, 2.8, 3.8, 4.8, 5.8]
(threshold = 0.25)
has_close_elements(numbers, threshold)  # Output should be True
``` 
This function uses the Set data structure to efficiently solve the problem. It compares the first and last elements of the list against each other, and if no elements are found in common, then the numbers are not close enough.