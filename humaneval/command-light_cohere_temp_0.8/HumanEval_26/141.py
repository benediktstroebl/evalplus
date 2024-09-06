```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize set to store unique integers
    duplicates = set()
    result = []

    # Loop through the list
    for num in numbers:
        if num not in duplicates:
            duplicates.add(num)
            result.append(num)

    return result

# Example usage
numbers = [1, 2, 3, 2, 4, 3, 1]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
``` 
This Python code defines a function `remove_duplicates` that removes duplicate elements from a list of integers. It uses the set data to keep track of unique integers and then constructs a new list with the remaining unique values. The example usage demonstrates the basic functionality of the function by providing a list of integers and the resulting unique numbers.