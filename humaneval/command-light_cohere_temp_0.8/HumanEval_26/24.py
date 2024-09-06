Here is a Python script that contains a self-contained function `remove_duplicates()`, which takes a list of integers as input and returns a new list with duplicate integers removed:
```python
from typing import List

def remove_duplicates(numbers: List[int]):
    # Initialize Set to store unique integers.
    seen = set()  # Create a set to keep track of seen integers
    result = []  # Initialize an empty list to store results

    # Loop through the input list
    for num in numbers:
        if num not in seen:
            seen.add(num)  # Add the element to seen set
            result.append(num)  # Append element to the result list
        else:
            result.remove(num)  # Remove duplicate element

    return(result)

# Test the function with sample input
test_input = [1, 2, 3, 2, 4]
result = remove_duplicates(test_input)
print(result)
```
This script defines a function `remove_duplicates()` that takes a list of integers as input and returns a new list with duplicate elements removed. The script also includes a test function `test_input` to verify the correctness of the `remove_duplicates()` function with the provided sample input.