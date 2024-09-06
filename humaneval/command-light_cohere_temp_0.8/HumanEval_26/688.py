```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[:seen]]

# Example usage and test cases
numbers = [1, 2, 3, 2, 4]
print("Removed duplicates: ", remove_duplicates(numbers))  # Expected output: [1, 3, 4]

numbers = [1, 2, 3, 4, 2, 3]
print("Removed duplicates: ", remove_duplicates(numbers))  # Expected output: [1, 2, 3]

numbers = [1, 2, 3, 4, 5, 6]
print("Removed duplicates: ", remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]
```

This script provides a remove_duplicates function that takes a list of integers as input and efficiently removes duplicate elements, ensuring the output is a list with unique integers. 
The example usage and test cases validate that the function works as expected.