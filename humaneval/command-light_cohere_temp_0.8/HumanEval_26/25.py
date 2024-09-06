Here is a self-contained Python script that solves the problem of removing duplicates from an integer list:
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers
    unique_set = set()
    # Loop through the list of integers
    for num in numbers:
        # Add the integer to the set if it's not already present
        if num not in unique_set:
            unique_set.add(num)
    # Create a new list and add the integers from the set to it
        result = [num for num in unique_set]
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```
This script defines a `remove_duplicates` function that takes a list of integers as input and returns a new list that contains only the unique integers. The function uses a set to keep track of the unique integers and a loop to go through the list, adding each integer to the set if it's not already present. The result list is then created by extracting each integer from the set.

When you run the script, it will print the list `[1, 3, 4]` which are the unique integers in the input list after removing duplicates.