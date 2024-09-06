```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers.
    unique_integers = set()

    # Loop through the input list and add elements to the set
    for num in numbers:
        unique_integers.add(num)

    # Create a new list with all elements from the set, in order of uniqueness
    return [num for num in unique_integers]

# Test the function
numbers = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(numbers)
print(result)

# Test with empty input
numbers = []
result2 = remove_duplicates(numbers)
print(result2)

# Test with duplicate elements
numbers = [1, 2, 2]
result3 = remove_duplicates(numbers)
print(result3)
```