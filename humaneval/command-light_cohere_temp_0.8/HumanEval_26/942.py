```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty list to store the unique numbers
    unique_numbers = []
    
    # Initialize an empty set to track the uniqueness of elements
    seen = set()
    
    for num in numbers:
        if num not in seen:
            seen.add(num)  # Add to seen set
            unique_numbers.append(num)  # Add to unique_numbers list
    return unique_numbers

# Example:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```
This code defines a function remove_duplicates that takes a list of integers as input and returns a new list that contains only the unique integers from the original input list. The function uses a set to track the uniqueness of elements and a new list to store the unique numbers. It iterates through elements through loop through the input list, and for each element, it checks if the element is already in the seen set. If the element is not seen, it is added to the seen set and to the unique_numbers list. The function returns the unique_numbers list as the output.