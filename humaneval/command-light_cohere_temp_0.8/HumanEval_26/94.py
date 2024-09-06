```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return [num for num in numbers if num not in numbers]

# Test the function with markdown code block
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
``` 
This function, named `remove_duplicates`, takes a list of integers as an input and returns a new list with elements that are not present in the input list more than once. The function first converts the to a set, which removes any duplicate elements, then converts the set back into a list and returns the elements that are not duplicates.